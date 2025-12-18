"""
QUESTION:
Construct a function named `find_vowel_locations` that takes a string `phrase` and a list of vowels `vowels` as input and returns a dictionary where the keys are the vowels and the values are lists of indices where each vowel appears in the phrase, ignoring case. The vowels should be located in their lower case form in the resulting dictionary.
"""

def find_vowel_locations(phrase, vowels):
    """
    Returns a dictionary where the keys are the vowels and the values are lists of indices where each vowel appears in the phrase, ignoring case.

    Args:
        phrase (str): The input string to search for vowels.
        vowels (list): A list of vowels to search for in the phrase.

    Returns:
        dict: A dictionary where the keys are the vowels and the values are lists of indices where each vowel appears in the phrase.
    """
    locations = {}
    for v in vowels:
        locations[v] = [i for i, letter in enumerate(phrase.lower()) if letter == v.lower()]
    return locations