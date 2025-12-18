"""
QUESTION:
Write a function least_frequent_letter that takes a string of lowercase alphabets as input and returns the least frequent letter in the string. If there are multiple least frequent letters, return any one of them.
"""

import collections

def least_frequent_letter(word):
    """
    This function returns the least frequent letter in a given string of lowercase alphabets.
    
    Parameters:
    word (str): The input string of lowercase alphabets.
    
    Returns:
    str: The least frequent letter in the string.
    """
    # Count the frequency of each letter
    counter = collections.Counter(word)
    
    # Get the letter with minimum frequency
    least_freq_letter = min(counter, key=counter.get)
    
    return least_freq_letter