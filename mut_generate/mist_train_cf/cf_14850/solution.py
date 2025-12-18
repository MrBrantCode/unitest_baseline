"""
QUESTION:
Write a function named `separate_string` that takes a string `s` as input and returns three substrings: one containing only consonants, one containing only vowels, and one containing any other characters. Assume vowels are 'a', 'e', 'i', 'o', 'u' in both lowercase and uppercase.
"""

def separate_string(s):
    """
    Separate a given string into three substrings: one containing only consonants, 
    one containing only vowels, and one containing any other characters.

    Parameters:
    s (str): The input string.

    Returns:
    tuple: A tuple containing three substrings: consonants, vowels, and other characters.
    """
    vowels = 'aeiouAEIOU'
    consonants = ''
    vowel_chars = ''
    other_chars = ''

    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_chars += char
            else:
                consonants += char
        else:
            other_chars += char

    return consonants, vowel_chars, other_chars