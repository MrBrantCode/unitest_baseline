"""
QUESTION:
Write a function `capitalize_vowels(input_str)` that takes a string of words as input and returns the string with all vowels capitalized. The function should only capitalize the vowels, leaving the consonants and other characters unchanged. The input string may contain any characters, but the function should only consider the vowels 'a', 'e', 'i', 'o', and 'u'. The function should not change the case of the vowels that are already capitalized.
"""

import re

def capitalize_vowels(input_str: str) -> str:
    vowels = "aeiou"
    modified_str = ''
    for char in input_str:
        if char.lower() in vowels:
            modified_str += char.upper()
        else:
            modified_str += char
    return modified_str