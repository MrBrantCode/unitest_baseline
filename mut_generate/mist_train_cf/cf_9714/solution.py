"""
QUESTION:
Write a function `longestCommonPrefix` that takes an array of strings `strs` as input and returns the longest common prefix string among all strings in the array. The longest common prefix must be at least 3 characters long. The input array can contain up to 100 strings, and each string can have a maximum length of 50 characters, containing both uppercase and lowercase letters, as well as special characters. If no common prefix of length 3 or more exists, return an empty string.
"""

def longestCommonPrefix(strs):
    prefix = ""
    
    if not strs or len(min(strs, key=len)) < 3:
        return prefix
    
    for i, c in enumerate(strs[0]):
        for s in strs[1:]:
            if i >= len(s) or s[i] != c:
                return prefix
        prefix += c
    
    return prefix