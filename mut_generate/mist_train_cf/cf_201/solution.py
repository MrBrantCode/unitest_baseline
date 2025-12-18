"""
QUESTION:
Write a function named `is_anagram` that takes two strings as parameters and returns True if the first string is an anagram of the second string, ignoring special characters and whitespace, and False otherwise. The function should have a time complexity of O(n), where n is the length of the strings, and a space complexity of O(1).
"""

def is_anagram(s1, s2):
    s1 = ''.join(char.lower() for char in s1 if char.isalnum())
    s2 = ''.join(char.lower() for char in s2 if char.isalnum())
    return sorted(s1) == sorted(s2)