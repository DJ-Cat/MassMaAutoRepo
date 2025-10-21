# src/parsing.py
import fitz  # PyMuPDF

def parse_pdf_to_text(file_path: str) -> str:
    """
    Extracts all text from a PDF file.

    Args:
        file_path: The path to the PDF document.

    Returns:
        A single string containing all extracted text from the document.
    """
    try:
        doc = fitz.open(file_path)
        full_text = ""
        for page in doc:
            full_text += page.get_text("text")
        doc.close()
        return full_text
    except Exception as e:
        print(f"Error parsing PDF {file_path}: {e}")
        return ""
