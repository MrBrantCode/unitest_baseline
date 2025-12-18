"""
QUESTION:
Write a function `check_anagram(str1, str2)` that checks if two input strings are anagrams. The function should ignore case, special characters, and whitespace. It should return `True` if the strings are anagrams, `False` otherwise. The input strings have a maximum length of 100 characters, and the function should have a time complexity of O(nlogn).
"""

def check_anagram(str1, str2):
    # Remove special characters and whitespace
    str1 = ''.join(c for c in str1 if c.isalnum())
    str2 = ''.join(c for c in str2 if c.isalnum())
    
    # Check if the lengths of the strings are different
    if len(str1) != len(str2):
        return False
    
    # Sort the strings
    sorted_str1 = sorted(str1.lower())
    sorted_str2 = sorted(str2.lower())
    
    # Check if the sorted strings are equal
    return sorted_str1 == sorted_str2