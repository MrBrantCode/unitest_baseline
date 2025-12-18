"""
QUESTION:
Write a function `get_unique_consonants` that takes two parameters: `first_sentence` and `second_sentence`, and returns the number of consonants present in the first sentence but not in the second. The function should be case-insensitive, treating 'b' and 'B' as the same letter.
"""

def get_unique_consonants(first_sentence, second_sentence):
    # define consonants
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    
    # get consonants from the first sentence
    consonants_in_first = set(c for c in first_sentence if c in consonants)
    
    # get consonants from the second sentence
    consonants_in_second = set(c for c in second_sentence if c in consonants)
    
    # get consonants that are only in the first sentence
    unique_consonants = consonants_in_first - consonants_in_second
    
    return len(unique_consonants)