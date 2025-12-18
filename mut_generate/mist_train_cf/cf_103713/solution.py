"""
QUESTION:
Create a function named `filter_vowel_start_words` that takes a string as input, splits the string into individual words, and returns a list of words that do not start with a vowel. The function should handle words with punctuation and be case-insensitive when checking for vowels.
"""

def filter_vowel_start_words(input_string):
    """
    This function filters out words that start with a vowel from a given string.

    Args:
        input_string (str): The input string to be processed.

    Returns:
        list: A list of words that do not start with a vowel.
    """
    return [word for word in input_string.split() if not word[0].lower() in 'aeiou']