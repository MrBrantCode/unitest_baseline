"""
QUESTION:
Write a function called "get_design_pattern_translation" that takes a language code as input and returns the translation of "Design Pattern" in that language. Assume the function will only be used with language codes for which a translation is available.
"""

def get_design_pattern_translation(language_code):
    """
    Returns the translation of "Design Pattern" in the given language.

    Args:
        language_code (str): The language code for the desired translation.

    Returns:
        str: The translation of "Design Pattern" in the given language.
    """
    translations = {
        'de': 'Entwurfsmuster',
        'es': 'Patrón de diseño',
        'pt': 'Padrão de projeto',
        'it': 'Pattern di progettazione',
        'pl': 'Wzorzec projektowy',
    }
    return translations.get(language_code)