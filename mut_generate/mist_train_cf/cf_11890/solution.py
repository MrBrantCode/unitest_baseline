"""
QUESTION:
Write a function called `findLongestSubstring` that takes a string as input and returns the length of the longest substring without repeating characters, considering whitespace characters as potential repeating characters. The function should handle strings with any characters and lengths.
"""

def findLongestSubstring(s: str) -> int:
    """
    This function calculates the length of the longest substring without repeating characters.
    
    Args:
        s (str): The input string.
    
    Returns:
        int: The length of the longest substring without repeating characters.
    """
    
    max_length = 0
    start_index = 0
    char_map = {}
    
    for index, ch in enumerate(s):
        if ch in char_map and char_map[ch] >= start_index:
            start_index = char_map[ch] + 1
            char_map = {k: v for k, v in char_map.items() if v >= start_index}
        
        char_map[ch] = index
        substring_length = index - start_index + 1
        max_length = max(max_length, substring_length)
    
    return max_length