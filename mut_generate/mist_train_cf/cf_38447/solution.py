"""
QUESTION:
Create a function `translate_to_chinese` that takes a list of tuples as input. Each tuple contains three elements: a tuple with an English phrase and additional instructions, a tuple of empty tuples, and a tuple containing a Chinese translation, additional instructions, and a tuple with a boolean confirmation status and additional data. The function should return a dictionary where the keys are the English phrases and the values are dictionaries containing the corresponding Chinese translations and their confirmation status.
"""

def translate_to_chinese(phrases):
    translations = {}
    for english, _, (chinese, _, (confirmed, _)) in phrases:
        english_phrase, _ = english
        translations[english_phrase] = {
            "translation": chinese,
            "confirmed": confirmed
        }
    return translations