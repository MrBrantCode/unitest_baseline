"""
QUESTION:
Implement a function `change_capitalization(text)` that changes the capitalization of a given text string, swapping the case of letters while ignoring numbers and preserving special characters and punctuation.
"""

def change_capitalization(text):
    return ''.join([char.upper() if char.islower() else char.lower() for char in text])