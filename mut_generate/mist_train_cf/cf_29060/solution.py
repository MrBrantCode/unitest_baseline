"""
QUESTION:
Write a function `max_consecutive_length(s: str) -> int` that takes a string `s` consisting of lowercase English letters and returns the length of the longest consecutive substring of the same character in `s`. The function should be able to handle empty strings.
"""

def max_consecutive_length(s: str) -> int:
    if not s:
        return 0
    
    max_length = 1
    temp_length = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            temp_length += 1
            max_length = max(max_length, temp_length)
        else:
            temp_length = 1
    
    return max_length