"""
QUESTION:
Write a function `longestCommonPrefix` that finds the longest common prefix string amongst an array of strings and returns the prefix along with the count of strings that have the common prefix. The function should be case-insensitive. If there is no common prefix, return an empty string and 0.

The input array `strs` contains 0 to 200 strings, each consisting of only lower-case and upper-case English letters with a maximum length of 200.
"""

def longestCommonPrefix(strs):
    if not strs:
        return ("", 0)
    
    shortest_str = min(strs, key=len)
    for i, char in enumerate(shortest_str):
        for other in strs:
            if other[i].lower() != char.lower():
                return (shortest_str[:i], i if i > 0 else 0) 
    return (shortest_str, len(strs))