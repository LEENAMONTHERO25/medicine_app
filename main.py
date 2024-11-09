import cv2
from PIL import Image
import pytesseract
import re
from extractor import extract_information
from language_detection import detect_language
from translator import translate_text
from google_search import get_additional_info  # Assuming you have a function for Google search.

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def capture_image():
    """Capture an image using the webcam."""
    cap = cv2.VideoCapture(0)
    print("Press 's' to capture an image.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break
        cv2.imshow("Capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            image_path = "captured_image.jpg"
            cv2.imwrite(image_path, frame)
            print("Image saved as captured_image.jpg")
            break
    cap.release()
    cv2.destroyAllWindows()
    return image_path

def preprocess_image(image_path):
    """Preprocess the image to improve OCR results."""
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    processed_image = cv2.medianBlur(thresh, 3)
    cv2.imwrite("processed_image_debug.png", processed_image)
    return processed_image

def extract_text(image_path):
    """Extract text from an image using OCR."""
    processed_image = preprocess_image(image_path)
    temp_image_path = "processed_image.png"
    cv2.imwrite(temp_image_path, processed_image)
    text = pytesseract.image_to_string(Image.open(temp_image_path), config="--psm 6")
    print("Raw OCR Text:")
    print(text)
    cleaned_text = re.sub(r'[^\x20-\x7E]+', '', text)
    print("\nCleaned OCR Text:")
    print(cleaned_text)
    return cleaned_text

def extract_medicine_name(text):
    """Extract only the name of the medicine from the OCR text."""
    name_match = re.search(r'\b[A-Za-z]+\b-?\d{0,3}', text)  # Adjust pattern as needed
    return name_match.group(0) if name_match else "Not found"

def main(target_language='en'):
    image_path = capture_image()
    text = extract_text(image_path)
    if text.strip():
        medicine_name = extract_medicine_name(text)
        print("\nExtracted Medicine Name:", medicine_name)
        
        if medicine_name != "Not found":
            additional_info = get_additional_info(medicine_name)  # Retrieve info from Google
            print("\nAdditional Information:")
            print(f"Details found at: {additional_info}")
        else:
            print("Medicine name not found in the text.")
    else:
        print("No text detected from the image.")

if __name__ == "__main__":
    main(target_language='en')
