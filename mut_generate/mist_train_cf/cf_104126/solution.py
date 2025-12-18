"""
QUESTION:
Create a function named `is_anagram` that takes two strings as input and returns a boolean indicating whether the two strings are anagrams of each other, considering letter case and whitespace. The function should return True if the strings are anagrams and False otherwise, assuming that an anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2):
        return False
    
    str1_chars = {}
    str2_chars = {}
    
    for char in str1:
        if char in str1_chars:
            str1_chars[char] += 1
        else:
            str1_chars[char] = 1
    
    for char in str2:
        if char in str2_chars:
            str2_chars[char] += 1
        else:
            str2_chars[char] = 1
    
    return str1_chars == str2_chars