"""
QUESTION:
Write a function `display_translation_status` that takes a dictionary of translations where the keys are language codes and the values are lists of translated strings. The function should return a dictionary where the keys are language codes and the values are the number of missing translations for each language. A missing translation is a string that is not present in the list of translations for a language but is present in the list of translations for the main language.

The input dictionary will have a key 'main' that represents the main language. All other keys represent international languages. The function should not modify the input dictionary.

The function should be able to handle dictionaries with any number of languages and any number of translations for each language.
"""

def display_translation_status(translations):
    """
    This function calculates the number of missing translations for each language in the given dictionary.

    Args:
    translations (dict): A dictionary where keys are language codes and values are lists of translated strings.
                         The dictionary should have a key 'main' representing the main language.

    Returns:
    dict: A dictionary where keys are language codes and values are the number of missing translations for each language.
    """
    
    # Initialize an empty dictionary to store the count of missing translations for each language
    missing_translations = {}

    # Get the list of translations for the main language
    main_translations = set(translations['main'])

    # Iterate over each language in the translations dictionary
    for language, translation_list in translations.items():
        # Skip the main language
        if language == 'main':
            continue
        
        # Calculate the missing translations for the current language
        missing_translations[language] = len(main_translations - set(translation_list))

    return missing_translations