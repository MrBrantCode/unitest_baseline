"""
QUESTION:
Write a function `longest_common_suffix(strs, ignoreCase=True)` that takes an array of strings `strs` and a boolean flag `ignoreCase` as input. The function should return a tuple containing the longest common suffix string amongst the array of strings and the count of strings that have the common suffix. The function should be case-insensitive if `ignoreCase` is `True` and case-sensitive otherwise. If there is no common suffix, the function should return an empty string and 0. The function should handle special characters and numbers in the strings. The input constraints are: `0 <= strs.length <= 200` and `0 <= strs[i].length <= 200`, where `strs[i]` consists of only lower-case and upper-case English letters, numbers, and special characters.
"""

def longest_common_suffix(strs, ignoreCase=True):
    if not strs:
        return ("", 0)
    min_length = min(len(s) for s in strs)
    common_suffix = ""
    count = 0
    for i in range(1, min_length+1):
        suffix = strs[0][-i:]
        if ignoreCase:
            if all(s.lower().endswith(suffix.lower()) for s in strs):
                common_suffix = suffix.lower()
                count = sum(1 for s in strs if s.lower().endswith(common_suffix))
            else:
                break
        else:
            if all(s.endswith(suffix) for s in strs):
                common_suffix = suffix
                count = sum(1 for s in strs if s.endswith(common_suffix))
            else:
                break
    return (common_suffix, count)