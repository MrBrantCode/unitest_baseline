"""
QUESTION:
Write a function named `evaluateStringCharDiff` that takes two strings, `txt1` and `txt2`, as input. The function should return `True` if the last character of `txt1` and the first character of `txt2` are alphabetical, not part of a word in their respective strings, and have an ASCII difference of 2 or less. The function should return `False` otherwise. If either `txt1` or `txt2` is empty, or if the last character of `txt1` or the first character of `txt2` is not alphabetical, the function should also return `False`.
"""

def evaluateStringCharDiff(txt1, txt2):
    if (not txt1 or not txt2 or 
        not txt1[-1].isalpha() or not txt2[0].isalpha()):
        return False
    if any(word.endswith(txt1[-1]) for word in txt1.split()) or any(word.startswith(txt2[0]) for word in txt2.split()):
        return False
    return abs(ord(txt1[-1]) - ord(txt2[0])) <= 2