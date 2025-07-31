from PyPDF2 import PdfReader
from typing import List
import re

class PDFProcessor:
    def extract_text(self, pdf_path: str) -> str:
        text = ""
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return self._clean_text(text)
    
    def _clean_text(self, text: str) -> str:
        # Remove excessive whitespace and special characters
        text = re.sub(r'\s+', ' ', text).strip()
        return text