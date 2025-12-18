"""
QUESTION:
Write a function `foo(x, y)` that takes two integers `x` and `y` and returns the sum of all `(i + j)` for `i` from 0 to `x-1` and `j` from 0 to `y-1`.
"""

def entrance(x, y):
    result = 0
    for i in range(x):
        for j in range(y):
            result += (i + j)
    return result