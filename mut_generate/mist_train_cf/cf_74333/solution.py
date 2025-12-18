"""
QUESTION:
Write a function `cycpattern_check(a, b)` that takes two string arguments and checks if string `b` or any of its rotational variations exists as a continuous subsequence in string `a`, ignoring case and non-alphabetic characters. The function should return `True` if a match is found and `False` otherwise.
"""

def cycpattern_check(a, b):
    import re

    # convert strings to lower case and remove all non-alphabetic characters
    a = re.sub('[^a-zA-Z]', '', a.lower())
    b = re.sub('[^a-zA-Z]', '', b.lower())

    # check if length of b is greater than a
    if len(b) > len(a):
        return False

    # generate all rotational patterns of b and check if any of them exists in a
    for i in range(len(b)):
        rotation = b[i:] + b[:i]
        if rotation in a:
            return True

    # if none of the rotations found, return False
    return False