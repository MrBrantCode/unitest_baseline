"""
QUESTION:
Write a function `longestCommonPrefix` that finds the longest common prefix string amongst its elements in a given array of strings. If there is no common prefix, return an empty string. The function should take a list of strings as input and return a string. The input list may be empty, and the function should handle this case by returning an empty string.
"""

from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""

    strs.sort()
    first = strs[0]
    last = strs[-1]
    prefix = ""
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            prefix += first[i]
        else:
            break

    return prefix