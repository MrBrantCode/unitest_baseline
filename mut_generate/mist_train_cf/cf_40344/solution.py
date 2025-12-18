"""
QUESTION:
Write a function `countNonSpaceChars` that takes a string `art` as input, where each line in the string is separated by a newline character and the string length is between 1 and 1000 (inclusive), and returns the count of non-space characters in the string.
"""

def countNonSpaceChars(art):
    """Return the count of non-space characters in a string."""
    count = 0
    for line in art.split('\n'):
        count += len([char for char in line if char != ' '])
    return count