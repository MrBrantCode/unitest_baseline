"""
QUESTION:
Create a function `identify_language(text, translations)` that takes a given text and a dictionary of languages with their corresponding translations. The function should return the language into which the given text is translated, considering variations in capitalization, punctuation, or spacing. The function should return "Language not found" if no match is found.
"""

def identify_language(text, translations):
    for language, translation in translations.items():
        if text.lower().replace(" ", "") == translation.lower().replace(" ", ""):
            return language
    return "Language not found."