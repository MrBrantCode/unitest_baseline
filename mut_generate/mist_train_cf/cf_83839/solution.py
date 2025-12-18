"""
QUESTION:
Define a function `O(n)` that calculates the number of distinct integer-sided equiangular octagons with a perimeter not exceeding `n`. The octagons are considered distinct if they are not congruent. The function should return the number of such octagons. Note that the sides of an equiangular octagon are all equal, so each side must be an integer between 1 and `n/8`.
"""

def O(n):
    return (n // 8)