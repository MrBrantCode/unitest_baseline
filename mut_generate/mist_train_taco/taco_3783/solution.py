"""
QUESTION:
Implement the function which should return `true` if given object is a vowel (meaning `a, e, i, o, u`), and `false` otherwise.
"""

def is_vowel(s: str) -> bool:
    """
    Determines if the given character is a vowel.

    Parameters:
    s (str): A single character string to check.

    Returns:
    bool: True if the character is a vowel (a, e, i, o, u), False otherwise.
    """
    return s.lower() in set('aeiou')