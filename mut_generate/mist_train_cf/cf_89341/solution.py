"""
QUESTION:
Write a function `is_anagram(s1, s2)` that checks if two given strings `s1` and `s2` are anagrams of each other. The function should consider all characters in the strings, including spaces and punctuation marks, and take their case into account. It should return `True` if the strings are anagrams and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the longer string, and should not use any built-in Python functions for sorting. The function should handle Unicode characters correctly and should be able to handle strings with a length up to 10^6 characters.
"""

def is_anagram(s1, s2):
    # Create dictionaries to store the character counts
    count1 = {}
    count2 = {}

    # Iterate over the characters in the first string
    for char in s1:
        # Update the count for this character
        count1[char] = count1.get(char, 0) + 1

    # Iterate over the characters in the second string
    for char in s2:
        # Update the count for this character
        count2[char] = count2.get(char, 0) + 1

    # Check if the count dictionaries are equal
    return count1 == count2