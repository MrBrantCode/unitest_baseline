"""
QUESTION:
Write a function called `longest_common_suffix` that takes a list of strings as input and returns the longest common suffix among all strings in the list. The function should be efficient enough to handle lists containing up to one million entries and maintain an optimal time complexity.
"""

def longest_common_suffix(strs):
    if not strs: return ""
    if len(strs) == 1: return strs[0]

    min_str = min(strs, key=len)

    for i in range(len(min_str), 0, -1):
        if all(s.endswith(min_str[-i:]) for s in strs):
            return min_str[-i:]

    return ""