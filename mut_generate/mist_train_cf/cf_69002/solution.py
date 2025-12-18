"""
QUESTION:
Create a function named `custom_mix_strings` that takes two strings `s1` and `s2` as input and returns a string. The function should perform a letter-wise interchange operation between the two strings up to the length of the shorter string, concatenate the resulting strings, and then invert the final string. If either of the input strings is empty, the function should return an empty string.
"""

from typing import Tuple

def custom_mix_strings(s1: str, s2: str) -> str:
    """ Meld two pieces of text by executing a letter-wise interchange operation, followed by an inversion of the final fused outcome
    """
    if len(s1) == 0 or len(s2) == 0:
        return ""

    s1, s2 = list(s1), list(s2)

    len_s1, len_s2 = len(s1), len(s2)
    
    min_len = min(len_s1, len_s2)
    
    # Alphabet-wise swapping
    for i in range(0, min_len):
        s1[i], s2[i] = s2[i], s1[i]
        
    # Concatenate the two strings
    melded_string = "".join(s1) + "".join(s2)
    
    # Invert the output
    return melded_string[::-1]