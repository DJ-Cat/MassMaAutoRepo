import fitz  # PyMuPDF
import spacy
import os

# Important: After installing requirements, you must download the spaCy model.
# Run this command in your terminal: python -m spacy download en_core_web_sm

def extract_text_from_pdf(pdf_path):
    """Extracts text from a given PDF file."""
    if not os.path.exists(pdf_path):
        return "Error: File not found at path: {}".format(pdf_path)
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        return f"Error processing PDF file: {e}"

def create_profile(text):
    """Creates a profile by extracting named entities from text using spaCy."""
    try:
        # Load the pre-trained spaCy model
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        print("Spacy model 'en_core_web_sm' not found.")
        print("Please run 'python -m spacy download en_core_web_sm' in your terminal.")
        return None

    doc = nlp(text)
    
    # Correctly initialize the profile dictionary
    profile = {
        'PERSON': [],      # People's names
        'ORG': [],         # Organizations, companies, schools
        'GPE': [],         # Geopolitical entities (cities, countries)
        'PRODUCT': [],     # Products, objects
        'EVENT': [],       # Named events
        'WORK_OF_ART': [], # Titles of books, songs etc.
        'LAW': [],         # Named laws, acts
        'LANGUAGE': [],    # Any named language
        'DATE': [],        # Absolute or relative dates or periods
        'TIME': [],        # Times of day
        'PERCENT': [],     # Percentage
        'MONEY': [],       # Monetary values
        'QUANTITY': [],    # Measurements, units
        'ORDINAL': [],     # "first", "second", etc.
        'CARDINAL': []     # Numerals that do not fall under another type.
    }

    for ent in doc.ents:
        if ent.label_ in profile:
            # Add the text of the entity, avoiding duplicates
            if ent.text.strip() not in profile[ent.label_]:
                profile[ent.label_].append(ent.text.strip())
                
    return profile
