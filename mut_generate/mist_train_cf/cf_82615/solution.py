"""
QUESTION:
Create a function called `find_maximum_even_divisible(x, y, z)` that takes three positive integers `x`, `y`, and `z` as input. The function should find the largest even integer in the inclusive range of `[x, y]` that is evenly divisible by `z`. If no such integer exists, the function should return `-1`. The function should not use any built-in functions or external libraries. Note that `x`, `y`, and `z` are assumed to be positive integers and `y` is greater than or equal to `x`.
"""

def find_maximum_even_divisible(x, y, z):
    for i in range(y, x-1, -1):
        if i % 2 == 0 and i % z == 0:
            return i
    return -1