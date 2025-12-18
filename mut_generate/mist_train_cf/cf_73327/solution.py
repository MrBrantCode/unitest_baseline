"""
QUESTION:
Write a function called `check_isogram` that takes a string as input and returns two boolean values. The function should check if the input string is an isogram (i.e., a word or phrase without a repeating letter) and a perfect isogram (i.e., a word or phrase in which every letter of the alphabet is used exactly once). The function should be case-insensitive and disregard any spaces or punctuation.
"""

import string

def check_isogram(input_str):
    """
    Checks if a given string is an isogram and a perfect isogram.
    
    Args:
    input_str (str): The input string to check.
    
    Returns:
    tuple: A tuple of two boolean values. The first value indicates whether the string is an isogram,
           and the second value indicates whether it is a perfect isogram.
    """
    
    # Converting string to lowercase and removing spaces and punctuation
    clean_str = ''.join(e for e in input_str if e.isalnum() or e.isspace()).replace(" ","").lower()
    
    # Check if string is an isogram
    is_isogram = len(clean_str) == len(set(clean_str))
    
    # Check if string is a perfect isogram
    is_perfect_isogram = set(clean_str) == set(string.ascii_lowercase)
    
    return is_isogram, is_perfect_isogram