"""
QUESTION:
Write a function `replace_spaces(s)` that takes a string `s` as input. The function should remove leading and trailing spaces from `s`, replace multiple consecutive spaces with a single '%20', and preserve the case of the input string. The output should be a string with all spaces replaced with '%20'.
"""

def replace_spaces(s):
    s = s.strip()
    s = s.split()
    return '%20'.join(s)