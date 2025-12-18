"""
QUESTION:
Write a function `is_anagram(str1, str2)` that determines if two input strings are anagrams of each other. The function should be case-insensitive, ignore any leading or trailing whitespace, and consider special characters. It should return `True` if the strings are anagrams and `False` otherwise. The strings can be of any length, but if they have different lengths, the function should immediately return `False`.
"""

def is_anagram(str1, str2):
    str1 = str1.strip().lower()
    str2 = str2.strip().lower()
    
    if len(str1) != len(str2):
        return False
    
    count = {}
    for char in str1:
        count[char] = count.get(char, 0) + 1
    for char in str2:
        count[char] = count.get(char, 0) - 1
    
    for char in count:
        if count[char] != 0:
            return False
    
    return True