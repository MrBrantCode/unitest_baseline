"""
QUESTION:
Write a function `chooseNum` that takes two positive integers `x` and `y` as input and returns the largest even integer within the range `[x, y]` inclusive. If no such number exists, return `-1`. The function should handle cases where `x` is greater than `y`.
"""

def chooseNum(x, y):
    """
    Returns the largest even integer within the range [x, y] inclusive.
    If no such number exists, returns -1.
    """
    if x > y:
        return -1
    y = y if y % 2 == 0 else y - 1
    for i in range(y, x - 1, -2):
        if i % 2 == 0:
            return i
    return -1