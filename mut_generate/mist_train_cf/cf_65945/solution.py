"""
QUESTION:
Create a function named `convert_first_letter_uppercase` that takes a string phrase as input, where each word is separated by a space. The function should return a new string where the first letter of each word is converted to uppercase and the rest of the letters remain unchanged.
"""

def convert_first_letter_uppercase(phrase):
    return ' '.join(word.capitalize() for word in phrase.split())