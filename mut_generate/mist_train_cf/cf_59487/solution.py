"""
QUESTION:
Create a function `check_anagrams(str1, str2)` that determines whether two given strings are anagrams of each other, considering the function case-sensitive and taking spaces and punctuation as characters.
"""

def check_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)