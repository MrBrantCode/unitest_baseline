"""
QUESTION:
Write a function `longest_substring_without_repeating_characters(s)` that takes a string `s` as input and returns the length of the longest contiguous substring without repeating characters in `s`. The function should be efficient and able to handle strings of any length.
"""

def longest_substring_without_repeating_characters(s):
    n = len(s)
    if n < 2:
        return n
    
    max_len = 0
    char_map = {}
    left = 0
    
    for right in range(n):
        if s[right] in char_map:    
            left = max(char_map[s[right]], left)
            
        max_len = max(max_len, right - left + 1)
        
        char_map[s[right]] = right + 1
    
    return max_len