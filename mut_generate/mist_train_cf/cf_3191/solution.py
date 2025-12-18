"""
QUESTION:
Write a function `longest_common_suffix` that finds the longest common suffix among all strings in a given list. If there is no common suffix, return an empty string. The function should take a list of strings as input and return the longest common suffix as a string.
"""

def longest_common_suffix(strings):
    if not strings:
        return ""

    min_len = min(len(s) for s in strings)
    common_suffix = ""

    for i in range(1, min_len + 1):
        suffix = strings[0][-i:]
        if all(s.endswith(suffix) for s in strings):
            common_suffix = suffix
        else:
            break

    return common_suffix