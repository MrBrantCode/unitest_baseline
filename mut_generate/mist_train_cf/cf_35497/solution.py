"""
QUESTION:
Implement a function `longestCommonPrefix(words)` that takes a list of strings `words` and returns the longest common prefix among all the strings. The input list `words` contains 1 to 200 strings, each with a length of 1 to 200 characters. If there is no common prefix, the function should return an empty string.
"""

def longestCommonPrefix(words):
    if not words:
        return ""
    
    prefix = min(words, key=len)
    for i, char in enumerate(prefix):
        for other in words:
            if other[i] != char:
                return prefix[:i]
    return prefix