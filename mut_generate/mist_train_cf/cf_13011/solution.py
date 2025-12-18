"""
QUESTION:
Create a function called `join_with_reverse` that takes two strings, `string1` and `string2`, and returns a single string. The returned string should be the concatenation of `string1`, the reverse of `string2`, and `string1` again.
"""

def join_with_reverse(string1, string2):
    return string1 + string2[::-1] + string1