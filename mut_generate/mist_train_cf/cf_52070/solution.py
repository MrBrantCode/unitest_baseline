"""
QUESTION:
Develop a function called `remove_consonants` that takes a string `sentence` as input and returns the string with all consonants removed. The function should be case-insensitive and consider all non-alphabetic characters as valid input.
"""

def remove_consonants(sentence):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    no_consonants = ''
    for char in sentence:
        if char not in consonants:
            no_consonants += char
    return no_consonants