import os
import sys
from ocr import extract_text_from_image, extract_text_from_pdf

def main(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    
    file_ext = os.path.splitext(file_path)[1].lower()
    
    if file_ext == '.pdf':
        text = extract_text_from_pdf(file_path)
    elif file_ext in ['.jpg', '.jpeg', '.png']:
        text = extract_text_from_image(file_path)
    else:
        print(f"Unsupported file type: {file_ext}")
        return
    
    if text:
        print('\n Extracted Text: \n')
        print(text)
    else:
        print("No text extracted")
        

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python danfe_extractor.py <file_path>")
    else:
        main(sys.argv[1])
        