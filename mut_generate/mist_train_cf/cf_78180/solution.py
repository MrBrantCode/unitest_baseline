"""
QUESTION:
Write a function called `transform_string(s)` that takes a string `s` as input and returns a transformed string where all whitespaces are replaced with underscores if the input string contains at least one whitespace; otherwise, it replaces all underscores with whitespaces.
"""

def transform_string(s):
    if " " in s:
        return s.replace(" ", "_")
    else:
        return s.replace("_", " ")