"""
QUESTION:
Write a function named `longest_common_prefix` that takes a list of strings as input and returns the longest common prefix string amongst the array of strings. The function should have a time complexity of O(n * m), where n is the number of strings in the array and m is the length of the longest string. The implementation should not use any built-in string comparison functions or data structures.
"""

def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = ""
    for i in range(len(strs[0])):
        for string in strs[1:]:
            if i >= len(string) or string[i] != strs[0][i]:
                return prefix
        prefix += strs[0][i]
    return prefix