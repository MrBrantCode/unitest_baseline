"""
QUESTION:
Write a function `find_combinations` that takes a string and an integer as input and returns the number of combinations of the given length from the characters in the string, considering that each character can only be used once in each combination. The string contains unique characters and the length of the combinations is less than or equal to the length of the string.
"""

import math

def find_combinations(s, length):
    """
    Calculate the number of combinations of a given length from the characters in a string.
    
    Parameters:
    s (str): The input string containing unique characters.
    length (int): The length of the combinations.
    
    Returns:
    int: The number of combinations of the given length.
    """
    return math.comb(len(s), length)