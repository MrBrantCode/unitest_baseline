"""
QUESTION:
Write a function named `join_strings` that takes two strings `string1` and `string2`, and a separator. The function should return a string that is the concatenation of `string1`, the separator, and `string2`, in descending order. However, it should return an error message if either `string1` or `string2` has fewer than 3 characters, or if the separator is a part of either `string1` or `string2`.
"""

def join_strings(string1, string2, separator):
    if len(string1) < 3 or len(string2) < 3:
        return "Both strings must have at least 3 characters."
    elif separator in string1 or separator in string2:
        return "Separator cannot be a part of either string."
    else:
        result = string1 + separator + string2
        return ''.join(sorted(result, reverse=True))