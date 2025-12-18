"""
QUESTION:
Create a function named `check_strings` that takes two string parameters, `s1` and `s2`, and determines the shared characters in both strings while ignoring their case. The function should return the shared characters and the number of occurrences of each shared character in both strings. Additionally, the function should check if one string is a permutation of the other. The function should not require any additional parameters other than `s1` and `s2`, and it should handle any type of string input.
"""

from collections import Counter

def check_strings(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    
    # Counter creates a dictionary of letter: count pairs
    dict1 = Counter(s1)
    dict2 = Counter(s2)

    # shared characters
    shared_chars = list((dict1 & dict2).elements())
    
    # counting occurrence
    combined = dict1 + dict2
    
    # check for permutation
    is_permutation = Counter(s1) == Counter(s2)
    
    return shared_chars, dict(combined), is_permutation