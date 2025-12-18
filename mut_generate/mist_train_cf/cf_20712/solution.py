"""
QUESTION:
Write a function called `is_anagram` that takes two strings as input and returns a boolean indicating whether the two strings are anagrams of each other. The function should ignore case sensitivity, whitespace characters, and special characters. It should also be efficient for large input strings.
"""

import re

def is_anagram(string1, string2):
    """
    This function checks if two strings are anagrams of each other.
    
    Args:
    string1 (str): The first string to compare.
    string2 (str): The second string to compare.
    
    Returns:
    bool: True if the strings are anagrams, False otherwise.
    """
    
    # Remove whitespace and special characters from both strings and convert to lowercase
    string1 = re.sub(r'\W+', '', string1).lower()
    string2 = re.sub(r'\W+', '', string2).lower()

    # If the lengths of the strings are not equal, they cannot be anagrams
    if len(string1) != len(string2):
        return False

    # Create a dictionary to store the count of each character in the first string
    char_count = {}

    # Count the characters in the first string
    for char in string1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Subtract the characters in the second string from the count
    for char in string2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False

    # If all counts are 0, the strings are anagrams
    return all(count == 0 for count in char_count.values())