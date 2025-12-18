"""
QUESTION:
Write a function named `are_anagrams` that determines if two given string inputs are anagrams of each other, considering case sensitivity. The function should return `True` if they are anagrams and `False` if they are not. The function should have a time complexity better than O(n log n).
"""

from collections import Counter

def are_anagrams(str1, str2):
    return Counter(str1) == Counter(str2)