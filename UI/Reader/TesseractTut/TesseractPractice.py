import pytesseract
from PIL import Image



def ocr_and_display(filepath):
    img = Image.open(filepath)
    ocr_result = pytesseract.image_to_string(img)
    print(ocr_result)

