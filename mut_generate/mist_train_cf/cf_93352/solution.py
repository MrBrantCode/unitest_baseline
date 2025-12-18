"""
QUESTION:
Write a function `convert_vowels_to_lowercase` that takes a string `text` as input and returns the modified string with all vowels in lowercase, regardless of their original case, while leaving consonants unchanged.
"""

def convert_vowels_to_lowercase(text):
    vowels = 'aeiou'
    converted_text = ''
    for char in text:
        if char.lower() in vowels:
            converted_text += char.lower()
        else:
            converted_text += char
    return converted_text