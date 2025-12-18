"""
QUESTION:
Write a function named `check_anagram` that takes two strings as input and returns True if they are anagrams, False otherwise. The function should handle cases with special characters, whitespace, and strings of up to 100 characters. It should not use any built-in string manipulation methods except for `isalnum()`, `len()`, `lower()`, and `sorted()`. The time complexity of the function should be O(nlogn).
"""

def check_anagram(str1, str2):
    str1 = ''.join(c for c in str1 if c.isalnum())
    str2 = ''.join(c for c in str2 if c.isalnum())
    if len(str1) != len(str2):
        return False
    return sorted(str1.lower()) == sorted(str2.lower())