"""
QUESTION:
Write a function `longest_common_prefix(strs)` that takes a list of strings `strs` and returns the longest common prefix among all strings in the list. The function should achieve a time complexity of O(n*m), where n is the number of strings in the list and m is the length of the longest string. The function must not utilize any built-in string matching functions.
"""

def entance(strs):
    if len(strs) == 0:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i][:len(prefix)] != prefix:
            prefix = prefix[:len(prefix) - 1]
            if prefix == "":
                return ""
    return prefix