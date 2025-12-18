"""
QUESTION:
Write a function named `word_occurrence_rate` that calculates the occurrence rate of individual words within a given textual string. The function should convert all words to lower case, remove punctuation, split the text into individual words, count the occurrence of each word, and return the word counts as a dictionary. The input string is assumed to contain only words and punctuation.
"""

from collections import Counter
import string

def word_occurrence_rate(text):
    """
    This function calculates the occurrence rate of individual words within a given textual string.
    
    Args:
    text (str): The input string to calculate word occurrence rates from.
    
    Returns:
    dict: A dictionary containing word counts.
    """
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    word_list = text.split()
    word_count = Counter(word_list)
    return dict(word_count)