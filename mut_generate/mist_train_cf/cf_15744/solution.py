"""
QUESTION:
Write a function `is_anagram(str1, str2)` that checks if two given strings are anagrams. The function should be case-sensitive, ignore any spaces or special characters, and consider the frequency of each character in the strings. It should return `True` only if both strings have the same frequency distribution of characters.
"""

def is_anagram(str1, str2):
    # Remove spaces and special characters and convert to lowercase
    str1 = ''.join(c for c in str1 if c.isalnum()).lower()
    str2 = ''.join(c for c in str2 if c.isalnum()).lower()

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