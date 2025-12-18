"""
QUESTION:
Write a function `longestSubstring(s)` that returns the longest substring of the given string `s` without repeating characters. If multiple substrings with the same length exist, return the lexicographically smallest one. The function should handle strings containing only lowercase English letters, be case-sensitive, and have a time complexity of O(n), where n is the length of the string.
"""

def longestSubstring(s):
    start = 0
    max_length = 0
    max_start = 0
    char_dict = {}
    
    for i in range(len(s)):
        if s[i] in char_dict and char_dict[s[i]] >= start:
            start = char_dict[s[i]] + 1
        
        char_dict[s[i]] = i
        
        if i - start + 1 > max_length:
            max_length = i - start + 1
            max_start = start
    
    return s[max_start:max_start+max_length]