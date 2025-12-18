"""
QUESTION:
Implement the function `longest_common_prefix(strs)` to find the longest common prefix string amongst an array of strings. The function should take an array of strings `strs` as input and return the longest common prefix string. The time complexity should be O(n * m), where n is the number of strings in the array and m is the length of the longest string.
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