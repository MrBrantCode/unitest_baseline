"""
QUESTION:
When provided with a String, capitalize all vowels

For example:

Input : "Hello World!"

Output : "HEllO WOrld!"

Note: Y is not a vowel in this kata.
"""

def capitalize_vowels(input_string: str) -> str:
    tr = str.maketrans('aeiou', 'AEIOU')
    return input_string.translate(tr)