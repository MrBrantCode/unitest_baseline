"""
QUESTION:
Implement a function `is_anagram(str1, str2)` that compares two input strings in a case-insensitive manner and checks if they are anagrams of each other. The function should return True if the strings are anagrams and False otherwise. The implementation should have a time complexity of O(n), where n is the length of the input strings.
"""

from collections import defaultdict

def is_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    if len(str1) != len(str2):
        return False
    
    count = defaultdict(int)
    
    for char in str1:
        count[char] += 1
    
    for char in str2:
        count[char] -= 1
        if count[char] < 0:
            return False
    
    return True