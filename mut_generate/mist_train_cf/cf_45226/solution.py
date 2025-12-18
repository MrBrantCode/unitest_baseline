"""
QUESTION:
Create a function called `remove_consonants` that takes a string `sentence` as input. The function should remove all consonants (including non-English and capitalized consonants) from the input sentence while preserving the original punctuation and spaces.
"""

def remove_consonants(sentence):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    no_consonants = ''.join(char for char in sentence if char.lower() not in consonants)
    return no_consonants