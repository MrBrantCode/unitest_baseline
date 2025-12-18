"""
QUESTION:
Create a function named `vowels_and_consonants` that takes a string `s` as input and returns a string containing the vowels and consonants from `s`, with each group ordered alphabetically. The function should consider both lowercase and uppercase letters, and ignore non-letter characters.
"""

def vowels_and_consonants(s):
    """
    Returns a string containing the vowels and consonants from the input string,
    with each group ordered alphabetically.

    :param s: Input string
    :return: String containing vowels and consonants
    """
    vowels = sorted([char for char in s.lower() if char in 'aeiou'])
    consonants = sorted([char for char in s.lower() if char.isalpha() and char not in 'aeiou'])
    return ''.join(vowels + consonants)