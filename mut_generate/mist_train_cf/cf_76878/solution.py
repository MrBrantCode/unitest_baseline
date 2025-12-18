"""
QUESTION:
Write a function `max_language_speakers` that takes a list of dictionaries as input, where each dictionary contains information about a language, including its name and number of native speakers. The function should return the name of the language with the maximum number of native speakers. Assume that the input list is non-empty and that each dictionary has the keys 'name' and 'speakers'.
"""

def max_language_speakers(languages):
    """
    Returns the name of the language with the maximum number of native speakers.

    Args:
    languages (list): A list of dictionaries, where each dictionary contains information about a language,
                      including its name and number of native speakers.

    Returns:
    str: The name of the language with the maximum number of native speakers.
    """
    max_speakers = 0
    max_language = ''

    for language in languages:
        if language["speakers"] > max_speakers:
            max_speakers = language["speakers"]
            max_language = language["name"]

    return max_language