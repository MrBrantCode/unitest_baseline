"""
QUESTION:
Write a function named `is_permutation` that takes two strings as input, reverses the order of characters in each string, and checks whether the reversed strings are permutations of each other. The function should return a boolean value indicating whether the reversed strings are permutations of each other. The time complexity of the function should be optimized.
"""

from collections import Counter

def is_permutation(str1, str2):
    # Reverse the strings
    str1 = str1[::-1]
    str2 = str2[::-1]
    
    # Create a frequency dictionary of characters for each string using Counter
    freq_dict1 = Counter(str1)
    freq_dict2 = Counter(str2)
    
    # Compare the frequency dictionaries
    # If they are the same, the strings are permutations of each other
    return freq_dict1 == freq_dict2