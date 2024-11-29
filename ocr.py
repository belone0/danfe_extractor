import pytesseract
from pdf2image import convert_from_path
from PIL import Image

def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang='por')
        return text
    except Exception as e:
        print(f"Error processing Image: {e} Image: {image_path}")
        return None
    
def extract_text_from_pdf(pdf_path):
    try:
        pages = convert_from_path(pdf_path)
        text = ''
        for page_number, page in enumerate(pages):
            page_text = pytesseract.image_to_string(page, lang='por')
            text += f"\n\n--- Page {page_number} ---\n\n{page_text}"
        return text
    except Exception as e:
        print(f"Error processing PDF: {e} PDF: {pdf_path}")
        return None