"""
QUESTION:
Create a function `organize_alphabets` that takes a string `s` as input, extracts and organizes its alphabetic characters in ascending lexicographical order, ignoring non-alphabetic characters and considering the sequence in a case-insensitive manner. The function should return a list of alphabetic characters.
"""

import re

def organize_alphabets(s):
    """
    This function takes a string s as input, extracts and organizes its alphabetic characters 
    in ascending lexicographical order, ignoring non-alphabetic characters and considering 
    the sequence in a case-insensitive manner.

    Args:
        s (str): The input string.

    Returns:
        list: A list of alphabetic characters.
    """
    # Extract alphabets only
    alphabets_only = re.sub("[^a-zA-Z]","",s)

    # Convert to a list
    alpha_list = list(alphabets_only)

    # Organize the list in ascending lexicographic order 
    final_list = sorted(alpha_list, key = lambda x:x.lower())

    return final_list