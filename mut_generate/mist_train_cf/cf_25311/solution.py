"""
QUESTION:
Write a function `longest_substring_without_repetition` that finds the length of the longest substring in a given string without repeating characters. The function should take a string as input and return an integer representing the length of the longest substring without repetition.
"""

def longest_substring_without_repetition(s: str) -> int:
    """
    This function finds the length of the longest substring in a given string without repeating characters.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The length of the longest substring without repetition.
    """
    chars = set()
    left = 0
    result = 0
    
    for right in range(len(s)):
        while s[right] in chars:
            chars.remove(s[left])
            left += 1
        chars.add(s[right])
        result = max(result, right - left + 1)
    
    return result