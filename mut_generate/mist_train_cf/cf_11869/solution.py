"""
QUESTION:
Write a function called "filter_words_and_calculate_avg_length" that takes a list containing both words and numbers as input and returns a tuple. The tuple should contain a list of only the words from the input list and the average length of these words, rounded up to the nearest integer. The input list may contain words of different lengths.
"""

import math

def filter_words_and_calculate_avg_length(mixed_list):
    """
    This function filters words from a mixed list, calculates the average length of the words, 
    and returns a tuple containing the list of words and the average word length rounded up.

    Args:
        mixed_list (list): A list containing both words and numbers.

    Returns:
        tuple: A tuple containing a list of words and the average word length rounded up.
    """

    words_list = [item for item in mixed_list if type(item) == str]
    avg_length = math.ceil(sum(len(word) for word in words_list) / len(words_list)) if words_list else 0
    
    return (words_list, avg_length)