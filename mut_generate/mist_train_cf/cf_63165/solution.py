"""
QUESTION:
Write a program with two functions, `perfect_cubes(n)` and `check_cube(n)`. The `perfect_cubes(n)` function should return a list of the first `n` perfect cubes. The `check_cube(n)` function should check if a given number `n` is a perfect cube and return True if it is, False otherwise. The program should not take any input and should only use the given functions.
"""

def entrance(n):
    def check_cube(num):
        cube_root = round(num ** (1. / 3))
        return cube_root ** 3 == num

    return [i ** 3 for i in range(1, n+1) if check_cube(i ** 3)]