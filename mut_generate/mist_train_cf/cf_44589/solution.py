"""
QUESTION:
Create a function called `purge_consonants` that takes a string `phrase` as input and returns a new string with all consonants removed. The function should preserve non-alphabetic characters and maintain their original positions.
"""

def purge_consonants(phrase):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in phrase if char in vowels or not char.isalpha()])