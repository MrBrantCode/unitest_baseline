"""
QUESTION:
Create a function `generate_sentences` that takes a list of words as input and returns all possible distinct sentences without any repetition of words in a sentence. The list of words can contain special characters or numbers. The function should be able to handle lists of varying lengths, but note that the number of possible sentences grows factorially with the length of the input list.
"""

import itertools

def generate_sentences(words):
    """
    Generate all possible distinct sentences without any repetition of words in a sentence.
    
    Args:
    words (list): A list of words that can contain special characters or numbers.
    
    Returns:
    list: A list of tuples, where each tuple is a permutation of the input list of words.
    """
    return list(itertools.permutations(words))