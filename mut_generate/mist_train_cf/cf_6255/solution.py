"""
QUESTION:
Write a Python function named `is_anagram(s1, s2)` that checks if two input strings `s1` and `s2` are anagrams of each other. The function should consider all characters in the strings, including spaces and punctuation marks, and take their case into account. The function should have a time complexity of O(n), where n is the length of the longer string, and should not use any built-in Python functions for sorting. It should correctly handle Unicode characters, strings with a length up to 10^6 characters, and should be case-sensitive.
"""

def is_anagram(s1, s2):
    # Create a dictionary to store the character counts
    count = {}

    # Iterate over the characters in the first string
    for char in s1:
        # Update the count for this character
        count[char] = count.get(char, 0) + 1

    # Iterate over the characters in the second string
    for char in s2:
        # If the character is not present in the count dictionary,
        # or if its count is already 0, return False
        if char not in count or count[char] == 0:
            return False
        # Otherwise, decrement the count for this character
        count[char] -= 1

    # Check if all counts in the dictionary are 0
    for val in count.values():
        if val != 0:
            return False

    # If all counts are 0, the strings are anagrams
    return True