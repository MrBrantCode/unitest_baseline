"""
QUESTION:
Create a function `create_dict` that takes a list of strings as input. The function should return a dictionary where the keys are the strings from the input list that meet the following conditions: 
- have a length between 1 and 20 characters, inclusive
- start with a lowercase letter
- contain at least one uppercase letter
- contain at least one special character from the set "!@#$%". Strings not meeting these conditions should be ignored. The values in the dictionary should be the lengths of the corresponding strings.
"""

def create_dict(strings):
    """
    Creates a dictionary from a list of strings. The keys are the strings 
    that have a length between 1 and 20 characters, start with a lowercase 
    letter, contain at least one uppercase letter, and contain at least one 
    special character from the set "!@#$%". The values are the lengths of 
    the corresponding strings.

    Args:
        strings (list): A list of strings.

    Returns:
        dict: A dictionary where the keys are the valid strings and the 
        values are their lengths.
    """
    result = {}
    for word in strings:
        if 1 <= len(word) <= 20 and word[0].islower() and any(char.isupper() for char in word) and any(char in "!@#$%" for char in word):
            result[word] = len(word)
    return result