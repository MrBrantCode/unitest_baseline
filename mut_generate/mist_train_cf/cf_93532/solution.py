"""
QUESTION:
Create a function `replace_odd_occurrences` that takes two parameters: `substring` and `replace_with`. This function should replace all occurrences of `substring` in the string with `replace_with`, but only if `substring` appears an odd number of times. If `substring` appears an even number of times or does not appear at all, the function should return the original string unchanged.
"""

def replace_odd_occurrences(string, substring, replace_with):
    count = string.count(substring)
    if count % 2 != 0:
        return string.replace(substring, replace_with)
    return string