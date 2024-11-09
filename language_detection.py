from langdetect import detect

def detect_language(text):
    language = detect(text)
    return language
