"""
QUESTION:
Write a function `translate_search_term(dictionary, search_term)` that takes a dictionary containing English to Portuguese translations and a search term in English as input. The function should return the Portuguese translation of the search term if it exists in the dictionary, or "Translation not found" if it does not.
"""

def translate_search_term(dictionary, search_term):
    """
    Translate a given English search term into Portuguese using a provided dictionary.
    
    Args:
        dictionary (dict): A dictionary containing English to Portuguese translations.
        search_term (str): The English search term to be translated.
    
    Returns:
        str: The Portuguese translation of the search term if found, otherwise "Translation not found".
    """
    return dictionary.get(search_term, "Translation not found")