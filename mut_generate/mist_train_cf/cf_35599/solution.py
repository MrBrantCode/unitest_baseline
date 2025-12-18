"""
QUESTION:
Write a function `longestCommonPrefix` that takes an array of strings as input and returns the longest common prefix as a string. The function should return an empty string if there is no common prefix among the strings in the array.
"""

def longestCommonPrefix(strs):
    if not strs:
        return ""

    # Sort the array of strings to easily find the common prefix
    strs.sort()

    # Compare the first and last strings to find the common prefix
    first = strs[0]
    last = strs[-1]
    prefix = ""
    for i in range(len(first)):
        if i < len(last) and first[i] == last[i]:
            prefix += first[i]
        else:
            break

    return prefix