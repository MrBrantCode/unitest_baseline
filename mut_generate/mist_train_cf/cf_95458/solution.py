"""
QUESTION:
Create a function `func` that takes a single argument `x` and returns an integer indicating whether `x` is positive (1), zero (0), negative (-1), or any other positive or negative integer if `x` is a float. If `x` is neither an integer nor a float, return "Invalid input".
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