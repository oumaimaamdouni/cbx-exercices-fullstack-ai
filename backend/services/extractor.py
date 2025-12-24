import re 
from models.cv_result import CVResult

def clean_text(text: str) -> str:
    """Nettoie le texte : enlève les espaces en trop et normalise."""
    text = re.sub(r'\s+', ' ', text)  
    text = re.sub(r'[^\w\s@.+-]', '', text)  
    return text.strip()

def extract_info(raw_text: str) -> CVResult:
    """Applique les Regex pour trouver les infos."""  
    text = clean_text(raw_text)

    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email = re.search(email_pattern, text)

    phone_pattern = r'(?:(?:\+|00)33|0)\s*[1-9](?:[\s.-]*\d{2}){4}'
    phone = re.search(phone_pattern, text)

    degrees_to_find = ["Master", "Bachelor", "Licence", "Doctorat", "Ingénieur", "Bac"]
    found_degree = None 
    for d in degrees_to_find:
        if re.search(rf'\b{d}\b', text, re.IGNORECASE):
            found_degree = d
            break

    words = text.split()
    first_name = words[0] if len(words) > 0 else None
    last_name = words[1] if len(words) > 1 else None

    return CVResult(
        first_name=first_name,
        last_name=last_name,
        email=email.group(0) if email else None,
        phone=phone.group(0) if phone else None,
        degree=found_degree
    )