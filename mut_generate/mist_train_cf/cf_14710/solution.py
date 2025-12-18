"""
QUESTION:
Create a function called `convert_vowels_to_lowercase` that takes a string `text` as input and returns a string where all vowels are in lowercase, while non-vowel characters remain unchanged, regardless of their original case.
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