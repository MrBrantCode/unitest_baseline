"""
QUESTION:
Write a function `invert_and_toggle` that takes a string of characters as input, reverses the order of the characters, and toggles the case of each character (from lowercase to uppercase and vice versa) without using any pre-existing "reverse" or "swapcase" functions. The function should return the modified string.
"""

def invert_and_toggle(text):
    result = ''
    for char in text:
        if char.isupper():
            result = char.lower() + result
        elif char.islower():
            result = char.upper() + result
        else:
            result = char + result
    return result