"""
QUESTION:
Given a string s, write a function lengthOfLongestSubstring(s) that returns the length of the longest substring with no repeating characters. If multiple substrings have the same maximum length, return the length of the first occurrence in the original string.
"""

def lengthOfLongestSubstring(s):
    start = 0
    end = 0
    unique_chars = set()
    maxLen = 0
    
    while end < len(s):
        if s[end] in unique_chars:
            unique_chars.remove(s[start])
            start += 1
        else:
            unique_chars.add(s[end])
            maxLen = max(maxLen, end - start + 1)
            end += 1
    
    return maxLen