"""
QUESTION:
Write a function called `word_frequency` that takes an input string, removes punctuation, converts it to lowercase, splits it into words, and returns a dictionary where keys are unique words and values are their corresponding frequencies.
"""

import string
from collections import Counter

def word_frequency(input_string):
    """
    This function takes an input string, removes punctuation, converts it to lowercase, 
    splits it into words, and returns a dictionary where keys are unique words and 
    values are their corresponding frequencies.
    """
    input_string = input_string.translate(str.maketrans("", "", string.punctuation))
    input_string = input_string.lower()
    word_list = input_string.split()
    return dict(Counter(word_list))