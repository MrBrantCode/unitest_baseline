"""
QUESTION:
Write a function called `is_anagram` that takes two strings as input and returns True if the first string is an anagram of the second string, and False otherwise. The function should ignore special characters and whitespace, and it should handle case-insensitive anagrams. The time complexity should be as close to O(n) as possible, where n is the length of the strings, and the space complexity should be O(1).
"""

def is_anagram(string1, string2):
    # Remove special characters and whitespace from both strings
    string1 = ''.join(char.lower() for char in string1 if char.isalnum())
    string2 = ''.join(char.lower() for char in string2 if char.isalnum())

    # Check if the sorted strings are equal
    return sorted(string1) == sorted(string2)