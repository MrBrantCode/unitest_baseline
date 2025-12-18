"""
QUESTION:
Write a function `longest_unique_substring` that takes a string as input and returns the length of the longest substring with unique characters. The input string contains only lowercase English alphabets (a-z). If there are multiple substrings with the same longest length, return the length of the first occurring substring.
"""

def longest_unique_substring(string):
    start = 0
    max_length = 0
    seen = {}
    
    for end, char in enumerate(string):
        if char in seen:
            start = max(start, seen[char] + 1)
        
        seen[char] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length