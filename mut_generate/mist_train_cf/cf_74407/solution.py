"""
QUESTION:
Design a function named `custom_merge_strings` that takes a tuple of three strings as input and returns a string. The function should merge the input strings by alternating characters from each string, prioritizing the strings based on their lengths. If the strings have different lengths, the characters from the shorter strings should be distributed among the characters of the longer string after the shorter strings are exhausted. Finally, the merged string should be reversed before being returned.
"""

from typing import Tuple
from itertools import zip_longest

def custom_merge_strings(strings: Tuple[str, str, str]) -> str:
    """
    Join three string entities by reciprocally selecting characters from each string, prioritizing the strings based on their lengths, and then inversing the resultant string.
    If a length mismatch occurs among the strings, the characters from the shorter string should smoothly incorporate among the characters of the elongated string post its exhaustion.
    """
    # Sort the strings based on their lengths
    sorted_strings = sorted(strings, key=len)
    
    # Alternate among the strings and join the characters 
    merged_string = [item for sublist in zip_longest(*sorted_strings) for item in sublist if item]
    
    # Inverse the resultant string
    inverted_string = merged_string[::-1]
    
    # Finally, join the result into a single string and return
    return "".join(inverted_string)