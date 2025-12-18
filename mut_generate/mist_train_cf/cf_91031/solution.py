"""
QUESTION:
Write a function `longestCommonPrefix(strs)` that takes an array of strings as input and returns the longest common prefix string. The longest common prefix string must be at least 3 characters long. The input array can contain up to 100 strings, each with a maximum length of 50 characters. The strings can contain both uppercase and lowercase letters, as well as special characters. If no common prefix of length at least 3 characters exists, return an empty string.
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