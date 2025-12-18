"""
QUESTION:
Write a function `process_string(s, p1, p2, join)` that takes a string `s` and two pairs of indices `p1` and `p2` as input, along with a boolean flag `join`. The function should return a substring based on the given indices. If `join` is `True`, the function should concatenate the substrings obtained from `p1` and `p2`. If `join` is `False`, the function should find the common characters in the two substrings. If there are no common characters, it should return an empty string. Assume that the indices are valid for the string and follow Python's 0-based index rule.
"""

def entrance(s: str, p1: tuple, p2: tuple, join: bool) -> str:
    if join:
        return s[p1[0]:p1[1]] + s[p2[0]:p2[1]]
    else:
        sub1, sub2 = set(s[p1[0]:p1[1]]), set(s[p2[0]:p2[1]])
        common = sub1.intersection(sub2)
        return ''.join(sorted(common))