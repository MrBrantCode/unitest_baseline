"""
QUESTION:
Create a function called `is_all_vowels` that takes a word as input and returns a boolean indicating whether the word is composed entirely of English vowels (both lowercase and uppercase), ignoring special characters and accent marks.
"""

def is_all_vowels(word):
    vowels = set('aeiou')
    return all(char.lower() in vowels for char in word if char.isalpha())