"""
QUESTION:
Write a function `compare_strings` that takes two strings `string1` and `string2` and an integer `n` as parameters. The function should return True if either of the strings, cropped to a maximum of `n` characters from the end, appears at the very end of the other string, ignoring upper/lower case differences.
"""

def compare_strings(string1, string2, n):
    try:
        return string1[-n:].lower() == string2.lower() or string2[-n:].lower() == string1.lower()
    except IndexError:
        return string1.lower() == string2.lower()