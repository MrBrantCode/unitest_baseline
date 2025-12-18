"""
QUESTION:
Implement a function `consonants_average(s)` that takes a string `s` as input and returns the average count of consonants present in the string. Consonants refer to all alphabets excluding 'a', 'e', 'i', 'o', 'u', and '.' when it appears in the middle of the word. Ignore the case of consonants and handle unusual symbols in the word. The function should handle empty strings and avoid division by zero errors.
"""

def consonants_average(s):
    """Calculate the average count of consonants in a given string.

    Consonants refer to all alphabets excluding 'a', 'e', 'i', 'o', 'u', and '.' 
    when it appears in the middle of the word. Ignore the case of consonants and 
    handle unusual symbols in the word.

    Args:
        s (str): The input string.

    Returns:
        float: The average count of consonants in the string.
    """
    consonants = [char for char in s.lower() if char.isalpha() and char not in ('a', 'e', 'i', 'o', 'u')]
    return len(consonants) / len(s) if s else 0