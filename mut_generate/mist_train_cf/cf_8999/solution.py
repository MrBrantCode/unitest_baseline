"""
QUESTION:
Write a function `longest_substring` that finds the longest substring of unique characters in a given string without using any built-in string functions or data structures. The function should return the longest substring of unique characters.
"""

def longest_substring(s):
    """
    Finds the longest substring of unique characters in a given string.
    
    Args:
        s (str): The input string.
    
    Returns:
        str: The longest substring of unique characters.
    """
    longest = ''
    current = ''
    last_occurrence = {}
    left = 0

    for right, char in enumerate(s):
        if char in last_occurrence and last_occurrence[char] >= left:
            left = last_occurrence[char] + 1
        last_occurrence[char] = right
        current = s[left:right + 1]
        if len(current) > len(longest):
            longest = current

    return longest