"""
QUESTION:
Write a function `is_all_vowels(s)` that determines if a given string `s` is composed entirely of vowels. The function should return `True` if the string is all vowels, `False` otherwise. If the string contains non-alphabetic characters, the function should return a message indicating the presence of non-alphabetic characters. The function should be case-insensitive and handle strings with a mix of English alphabets, digits, symbols, and whitespaces.
"""

def is_all_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    s = s.lower()

    if not s.isalpha():
        return f"The string '{s}' contains non-alphabetic characters."

    for letter in s:
        if letter not in vowels:
            return False
            
    return True