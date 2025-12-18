"""
QUESTION:
Write a function named `longest_common_prefix` that takes a list of strings as input and returns the longest common prefix among all strings in the list. The function should handle special characters and numbers, and consider strings as case-sensitive. If the input list is empty, the function should return an empty string.
"""

def longest_common_prefix(strs):
    if not strs:
        return ""
    shortest = min(strs,key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest