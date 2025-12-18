"""
QUESTION:
Write a function `is_anagram(str1, str2)` that checks if two input strings are anagrams of each other, ignoring special characters, whitespace, and case differences. The function should not use any built-in string manipulation methods or libraries, except for `len()` and `lower()`. It should return `True` if the strings are anagrams and `False` otherwise.
"""

def entrance(str1, str2):
    # Remove special characters and whitespace from both strings
    str1 = ''.join(e for e in str1 if e.isalnum())
    str2 = ''.join(e for e in str2 if e.isalnum())

    # Check if the length of both strings are equal
    if len(str1) != len(str2):
        return False

    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Create dictionaries to store character frequencies
    char_freq1 = {}
    char_freq2 = {}

    # Count the frequency of each character in str1
    for char in str1:
        if char in char_freq1:
            char_freq1[char] += 1
        else:
            char_freq1[char] = 1

    # Count the frequency of each character in str2
    for char in str2:
        if char in char_freq2:
            char_freq2[char] += 1
        else:
            char_freq2[char] = 1

    # Check if the frequency of each character is the same in both strings
    for char in char_freq1:
        if char not in char_freq2 or char_freq1[char] != char_freq2[char]:
            return False

    return True