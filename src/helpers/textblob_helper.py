from textblob import TextBlob

LANGUAGES = {
    'ar': 'ar', 
    'de': 'de', 
    'en': 'en', 
    'es': 'es', 
    'fr': 'fr', 
    'he': 'iw', 
    'it': 'it', 
    'nl': 'nl', 
    'no': 'no', 
    'pt': 'pt', 
    'ru': 'ru', 
    'se': 'sv', 
    'zh': 'zh'
}

def translate(text: str, to_lang: str, from_lang: str):
    return str(TextBlob(text).translate(from_lang, to_lang))