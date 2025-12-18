"""
QUESTION:
Write a function `gcdOfStrings` that takes two strings `str1` and `str2` as input and returns the longest string that can divide both `str1` and `str2` by concatenating with itself. The length of `str1` and `str2` should be between 1 and 1000, inclusive, and both are composed of English uppercase letters.
"""

def gcdOfStrings(str1: str, str2: str) -> str:
    if len(str1) < len(str2):
        return gcdOfStrings(str2, str1)
    elif not str1.startswith(str2):   
        return ''   
    elif str2 == '':
        return str1
    else:
        return gcdOfStrings(str1[len(str2):], str2)