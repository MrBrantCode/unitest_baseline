"""
QUESTION:
Create a function named `convert_vowels` that takes a string `text` as input and returns the modified string after applying the following transformations: all vowels (both lowercase and uppercase) are converted to uppercase, all consonants are converted to lowercase, and all duplicate vowels are removed from the string.
"""

def convert_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    modified_text = ''
    for char in text:
        if char.lower() in vowels and char.lower() not in modified_text:
            modified_text += char.upper()
        elif char.lower() not in vowels:
            modified_text += char.lower()
    return modified_text