"""
QUESTION:
Write a function `longestCommonPrefix` that takes two parameters: a list of strings `strs` and an optional boolean flag `ignoreCase` with a default value of `True`. The function should find the longest common prefix string amongst the input strings in a case-sensitive or case-insensitive manner, depending on the value of `ignoreCase`. If there is no common prefix, the function should return an empty string. Additionally, the function should return the count of strings that have the common prefix. The input strings may contain special characters and numbers, and the function should be able to handle them correctly. The length of the input list `strs` is between 0 and 200, and the length of each string in `strs` is between 0 and 200.
"""

def longestCommonPrefix(strs, ignoreCase=True):
    prefix = ''
    prefix_count = 0

    if ignoreCase:
        strs = [s.lower() for s in strs]

    for tuple in zip(*strs):
        if len(set(tuple)) == 1:
            prefix += tuple[0]
            prefix_count = len([s for s in strs if s.startswith(prefix)])
        else:
            break

    return prefix, prefix_count