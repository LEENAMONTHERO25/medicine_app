from PIL import Image, ImageFilter, ImageOps

def preprocess_image(image_path):
    image = Image.open(image_path)
    # Convert to grayscale
    image = image.convert("L")
    # Increase contrast
    image = ImageOps.autocontrast(image)
    # Apply a threshold to binarize the image
    image = image.point(lambda x: 0 if x < 128 else 255, '1')
    return image
