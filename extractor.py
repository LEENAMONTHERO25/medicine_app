import re

def extract_information(text):
    # Update regex to look for keywords and capture associated information
    name = re.search(r"(?:tablet|capsule|medicine|product)[\s\w-]*(\w+[\w\s-]+)", text, re.IGNORECASE)
    dosage = re.search(r"(\d+\s*(mg|g|ml|mcg|unit))", text, re.IGNORECASE)
    usage = re.search(r"(?:for\s*)?([A-Za-z\s]+[.]?)", text)  # Capture usage info like "for headaches"
    side_effects = re.search(r"side effects?[:\s]*([\w\s,]+)", text, re.IGNORECASE)

    return {
        "Name": name.group(1) if name else "Not found",
        "Dosage": dosage.group(1) if dosage else "Not found",
        "Usage": usage.group(1) if usage else "Not found",
        "Side Effects": side_effects.group(1) if side_effects else "Not found"
    }
