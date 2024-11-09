from googletrans import Translator  # Import the required library

def translate_text(text, source_language, target_language):
    translator = Translator()
    translation = translator.translate(text, src=source_language, dest=target_language)
    return translation.text
