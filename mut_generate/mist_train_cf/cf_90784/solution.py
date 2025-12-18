"""
QUESTION:
Write a function `is_anagram(str1, str2)` that checks whether two input strings `str1` and `str2` are anagrams of each other. The function should ignore case differences, whitespace, special characters, and numbers. It should return `True` if the strings are anagrams and `False` otherwise.
"""

def is_anagram(str1, str2):
    # Remove whitespace and convert both strings to lowercase
    str1 = ''.join(str1.lower().split())
    str2 = ''.join(str2.lower().split())
    
    # Remove special characters and numbers from both strings
    str1 = ''.join(ch for ch in str1 if ch.isalpha())
    str2 = ''.join(ch for ch in str2 if ch.isalpha())
    
    # Sort both strings alphabetically
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))
    
    # Compare the sorted strings
    return str1 == str2