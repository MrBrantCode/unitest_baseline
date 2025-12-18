"""
QUESTION:
Implement a function `longest_common_prefix` that takes a list of strings `strs` as input and returns the longest common prefix string amongst the strings in the list. If there is no common prefix, the function should return an empty string. The function should be efficient and able to handle lists of varying lengths and string sizes.
"""

from typing import List

def longest_common_prefix(strs: List[str]) -> str:
    if not strs:
        return ""

    strs.sort()
    first = strs[0]
    last = strs[-1]
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1

    return first[:i]