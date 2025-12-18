"""
QUESTION:
Write a function named `longest_substring_length` that takes a string as input and returns an integer representing the length of the longest substring with no repeated characters. The substring must be contiguous and the characters must appear in the same order as in the original string.

The input string can contain both lowercase and uppercase letters, as well as special characters, and its length will be at most 10^5 characters. The solution should have a time complexity of O(n), where n is the length of the input string. If there are multiple longest substrings with no repeated characters, return the length of the first one encountered.
"""

def longest_substring_length(s):
    start = 0
    end = 0
    seen = set()
    longest_length = 0
    
    while end < len(s):
        if s[end] not in seen:
            seen.add(s[end])
            longest_length = max(longest_length, end - start + 1)
            end += 1
        else:
            seen.remove(s[start])
            start += 1
    
    return longest_length