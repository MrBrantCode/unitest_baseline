"""
QUESTION:
Implement a function `is_permutation(str1, str2)` that determines whether two input strings are permutations of each other. The function should return a boolean value indicating whether the strings are permutations. The function must run in linear time, O(n), where n is the length of the input strings.
"""

from collections import Counter

def is_permutation(str1, str2): 
    if len(str1) != len(str2): 
        return False
  
    return Counter(str1) == Counter(str2)