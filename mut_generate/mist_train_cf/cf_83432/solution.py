"""
QUESTION:
Write a function `remove_special_characters_and_numbers` that takes a string as input and returns a new string with all special characters and numbers removed, all uppercase letters converted to lowercase, and the original order of the alphabets preserved.
"""

def remove_special_characters_and_numbers(s):
    return ''.join([char.lower() for char in s if char.isalpha()])