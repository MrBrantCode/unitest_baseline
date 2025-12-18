"""
QUESTION:
Implement a function `strStr(haystack, needle)` that returns the starting index of the first occurrence of the substring `needle` in the string `haystack`. If `needle` is not found in `haystack`, return -1. The function should not use any built-in string search functions.
"""

def strStr(haystack, needle):
    if not needle:
        return 0  

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i : i + len(needle)] == needle:
            return i

    return -1 