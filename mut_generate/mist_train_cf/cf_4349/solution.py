"""
QUESTION:
Find the length of the longest substring without repeating characters in a given string. The function should consider all characters, including whitespace, special characters, and numbers, as potential repeating characters. 

Implement a function named `length_of_longest_substring` that takes a string as input and returns the length of the longest substring without repeating characters.
"""

def length_of_longest_substring(s: str) -> int:
    """
    This function calculates the length of the longest substring without repeating characters.
    
    Args:
    s (str): The input string.
    
    Returns:
    int: The length of the longest substring without repeating characters.
    """
    char_dict = {}
    start = 0
    max_length = 0
    
    for end, char in enumerate(s):
        if char in char_dict and char_dict[char] >= start:
            start = char_dict[char] + 1
        max_length = max(max_length, end - start + 1)
        char_dict[char] = end
        
    return max_length