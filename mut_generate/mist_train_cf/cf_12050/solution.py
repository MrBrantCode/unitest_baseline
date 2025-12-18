"""
QUESTION:
Create a function named `count_non_vowel_chars` that takes a string `s` as input and returns a dictionary where keys are characters from the string and values are their occurrences, excluding vowels (case-sensitive). The function should treat uppercase and lowercase versions of the same character as separate characters.
"""

def count_non_vowel_chars(s):
    """
    This function takes a string `s` as input and returns a dictionary where keys are characters from the string 
    and values are their occurrences, excluding vowels (case-sensitive). The function treats uppercase and 
    lowercase versions of the same character as separate characters.

    Args:
        s (str): The input string.

    Returns:
        dict: A dictionary with characters as keys and their occurrences as values.
    """
    dictionary = {}
    for char in s:
        if char.lower() not in 'aeiou':
            dictionary[char] = dictionary.get(char, 0) + 1
    return dictionary