from translate import Translator

LANGUAGES = ['ar', 'de', 'en', 'es', 'fr', 'he', 'it', 'nl', 'no', 'pt', 'ru', 'se', 'zh']

def translate(text, to_lang, from_lang='en'):
    return Translator(to_lang, from_lang).translate(text)