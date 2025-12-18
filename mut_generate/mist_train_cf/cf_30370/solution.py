"""
QUESTION:
Given a positive integer n, write a function `count_square_laminae` that returns the number of different square laminae that can be formed using up to n tiles, where a square lamina is a square outline with a square "hole" possessing vertical and horizontal symmetry.
"""

import math

def count_square_laminae(n: int) -> int:
    count = 0
    for outer_side in range(1, int(math.sqrt(n / 4)) + 1):
        inner_side = outer_side - 2
        while outer_side ** 2 - inner_side ** 2 <= n and inner_side >= 1:
            count += 1
            inner_side -= 2
    return count