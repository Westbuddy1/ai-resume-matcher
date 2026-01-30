
# resume_parser.py
import os
from typing import Union

try:
    from PyPDF2 import PdfReader
except ImportError:
    PdfReader = None


def extract_text(file_path: str) -> str:
    """
    Extracts text from a PDF or plain text file.
    """
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    if ext == ".pdf":
        if PdfReader is None:
            raise ImportError("PyPDF2 is required to parse PDFs")
        text = ""
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()

    elif ext in [".txt"]:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    else:
        raise ValueError("Unsupported file type. Only PDF or TXT allowed.")
