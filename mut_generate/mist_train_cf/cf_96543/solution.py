"""
QUESTION:
Define a function named `is_anagram` that takes two strings as input. The function should determine if the first string is an anagram of the second string, ignoring case, whitespace, and punctuation. It should return `True` if the strings are anagrams, and `False` otherwise. The time complexity of the function should be O(nlogn), and the space complexity should be O(1) or O(n).
"""

import string

def is_anagram(str1, str2):
    # Remove whitespace and punctuation
    str1 = str1.translate(str.maketrans("", "", string.whitespace + string.punctuation))
    str2 = str2.translate(str.maketrans("", "", string.whitespace + string.punctuation))
    
    # Convert to lowercase
    str1 = str1.lower()
    str2 = str2.lower()
    
    # Sort strings alphabetically
    str1_sorted = ''.join(sorted(str1))
    str2_sorted = ''.join(sorted(str2))
    
    # Compare sorted strings
    return str1_sorted == str2_sorted