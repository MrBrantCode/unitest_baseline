"""
QUESTION:
Write a function named `end_other` that takes two string parameters. The function should return `True` if either of the strings appears at the very end of the other string, ignoring upper/lower case differences. The function should have a time complexity of O(n), where n is the length of the longer string, and a space complexity of O(1).
"""

def end_other(a, b):
    a = a.lower()
    b = b.lower()

    if len(a) < len(b):
        return b.endswith(a)
    else:
        return a.endswith(b)