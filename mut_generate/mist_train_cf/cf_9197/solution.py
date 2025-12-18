"""
QUESTION:
Write a function `is_anagram(str1, str2)` that takes two strings as input, removes any whitespace and special characters, converts the strings to lowercase, and checks if they are anagrams of each other. The function should return True if the strings are anagrams and False otherwise.
"""

def entrance(str1, str2):
    str1 = ''.join(ch for ch in str1 if ch.isalpha()).lower()
    str2 = ''.join(ch for ch in str2 if ch.isalpha()).lower()
    
    return sorted(str1) == sorted(str2)