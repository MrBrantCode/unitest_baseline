"""
QUESTION:
Create a function `longestSubstringWithoutDuplication` that takes a string as input and returns the longest substring without any repeated characters. The function should only consider substrings with unique characters.
"""

def longestSubstringWithoutDuplication(string): 
    longest = "" 
    start = 0 
    seen = {} 
      
    for i, char in enumerate(string): 
        if char in seen and start <= seen[char]: 
            start = seen[char] + 1
        seen[char] = i 
        longest = max(longest, string[start:i + 1], key = len) 
      
    return longest