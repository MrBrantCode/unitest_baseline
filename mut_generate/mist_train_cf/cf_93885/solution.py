"""
QUESTION:
Write a function `is_anagram` that takes two strings as input and returns `True` if the strings are anagrams of each other, `False` otherwise. The function should be case-sensitive, ignore any non-alphanumeric characters, and consider the frequency of each character. The function should return `True` only if both strings have the same frequency distribution of characters.
"""

def is_anagram(str1, str2):
    # Remove spaces and special characters 
    str1 = ''.join(c for c in str1 if c.isalnum())
    str2 = ''.join(c for c in str2 if c.isalnum())

    # Create dictionaries to store character frequencies
    freq1 = {}
    freq2 = {}

    # Calculate frequency of each character in str1
    for char in str1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1

    # Calculate frequency of each character in str2
    for char in str2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1

    # Check if the frequency distributions are the same
    return freq1 == freq2