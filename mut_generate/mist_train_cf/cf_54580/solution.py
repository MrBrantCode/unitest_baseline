"""
QUESTION:
Design a function `check_consonants` that accepts a list of strings. The function should return `True` if the first letter of each string in the list is a consonant (assuming 'y' is not a vowel), and `False` otherwise.
"""

def check_consonants(lst):
    vowels = 'aeiouAEIOU'
    return all(word[0] not in vowels for word in lst)