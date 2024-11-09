import pytesseract
from PIL import Image

# Ensure Tesseract's path is set
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image):
    try:
        # Use configuration to specify OCR options
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(image, config=custom_config)
    except Exception as e:
        print("Error during OCR processing:", e)
        text = ""
    return text
    print("\nOCR Extracted Text:")
    print(text)  # Check if any text was captured

