"""
QUESTION:
Write a function `least_recurrent_character` that takes a sentence as input and returns the character that appears least frequently in the sentence. The function should ignore spaces, consider 'A' and 'a' as different characters, and treat punctuation marks and numbers as characters. If there are multiple least recurrent characters, the function should return any one of them.
"""

from collections import Counter

def least_recurrent_character(sentence):
    """
    This function finds the character that appears least frequently in a given sentence.
    
    Args:
        sentence (str): The input sentence.
    
    Returns:
        str: A character that appears least frequently in the sentence.
    """
    sentence = sentence.replace(" ", "")  # Remove spaces
    counter = Counter(sentence)
    return counter.most_common()[-1][0]