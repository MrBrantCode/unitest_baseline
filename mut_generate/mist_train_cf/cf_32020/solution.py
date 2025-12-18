"""
QUESTION:
Write a function `count_subgrids` that takes three integers `n`, `h`, and `w` as input where 1 ≤ `h` ≤ `n` and 1 ≤ `w` ≤ `n`, and returns the number of subgrids in an n x n grid that have a height of `h` and a width of `w`.
"""

def count_subgrids(n, h, w):
    return (n - h + 1) * (n - w + 1)