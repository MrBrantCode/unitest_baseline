"""
QUESTION:
Implement the `longestCommonPrefix` function that takes a list of strings as input and returns the longest common prefix among all the strings. If there is no common prefix, return an empty string. The function should be able to handle an empty input list and should not assume any specific length or content for the input strings. The function signature is `def longestCommonPrefix(strs: List[str]) -> str:`
"""

from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""

    strs.sort()
    first = strs[0]
    last = strs[-1]
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1

    return first[:i]