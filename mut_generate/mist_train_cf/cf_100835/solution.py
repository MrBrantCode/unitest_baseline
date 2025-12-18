"""
QUESTION:
Design an algorithm to determine whether two given strings are anagrams of each other. Implement the solution in a function called `is_anagram(str1, str2)` that takes two strings as input and returns a boolean indicating whether they are anagrams or not. The function should ignore case sensitivity and any spaces in the input strings.
"""

def is_anagram(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    return sorted(str1) == sorted(str2)