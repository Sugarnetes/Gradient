import os
from pdf2image import convert_from_path
import pytesseract

# Ensure poppler_path points to the directory containing bin
poppler_path = r"C:\Program Files\poppler-23.11.0\library\bin"

# Tesseract installation directory
tesseract_path = r"C:\Program Files\Tesseract-OCR"

# Add Tesseract to PATH
os.environ['PATH'] += os.pathsep + tesseract_path

class PdfReader():
    def __init__(self, file_name):
        self.file_name = file_name

    def extractor(self):
        # Extract text from PDF using pdf2image and pytesseract
        pages = convert_from_path(self.file_name, poppler_path=poppler_path)
         
        for i, page in enumerate(pages):
            text = pytesseract.image_to_string(page)
            print(f"Page {i + 1} - {text}")

if __name__ == "__main__":
    pdfTest = PdfReader(r"C:\umer files\Programming PREJE'S\Medicall\server\restapis\Fruit (1).pdf")
    pdfTest.extractor()