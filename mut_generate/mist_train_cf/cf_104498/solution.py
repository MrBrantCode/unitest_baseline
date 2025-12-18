"""
QUESTION:
Write a function `func(x)` that takes a single input `x` and returns an integer. If `x` is an integer, return 1 if `x` is positive, 0 if `x` is zero, and -1 if `x` is negative. If `x` is a float, return its integer representation. If `x` is neither an integer nor a float, return "Invalid input".
"""

def func(x):
    if isinstance(x, int):
        if x < 0:
            return -1
        elif x == 0:
            return 0
        elif x > 0:
            return 1
    elif isinstance(x, float):
        return int(x)
    else:
        return "Invalid input"