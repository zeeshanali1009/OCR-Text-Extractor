import pytesseract
from PIL import Image
from io import BytesIO
import os
from dotenv import load_dotenv

# Load .env if needed
load_dotenv()

# If tesseract is not in PATH, set it here:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_bytes):
    try:
        img = Image.open(BytesIO(image_bytes))
        text = pytesseract.image_to_string(img)
        return text.strip() or "No text found in image."
    except Exception as e:
        return f"Error extracting text: {str(e)}"
