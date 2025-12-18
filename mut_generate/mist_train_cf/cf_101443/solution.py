"""
QUESTION:
Write a function `parse_translation_data` that takes a JSON string as input, parses it, and returns the French and English translations. The JSON string should contain the translations for the French greeting phrase "Bonjour, comment allez-vous?" in the following format: `{"greeting": {"french": string, "english": string}}`. The function should return the French and English translations as strings.
"""

import json

def parse_translation_data(json_string):
    """
    This function takes a JSON string, parses it and returns the French and English translations.
    
    Args:
        json_string (str): A JSON string containing the translations.
    
    Returns:
        tuple: A tuple containing the French and English translations as strings.
    """
    parsed_data = json.loads(json_string)
    french_translation = parsed_data['greeting']['french']
    english_translation = parsed_data['greeting']['english']
    return french_translation, english_translation