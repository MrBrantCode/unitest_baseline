"""
QUESTION:
Write a function named `solve` that takes an integer `N` as input and returns the number of primitive triangles with integer sides whose combined side lengths, or perimeter, do not surpass `N`. A triangle with integer sides `(a, b, c)` is designated as primitive if the greatest common divisor of `a`, `b`, and `c` equals `1`. The function should be efficient and able to handle large values of `N`.
"""

def solve(N):
    """
    This function calculates the number of primitive triangles with integer sides 
    whose combined side lengths, or perimeter, does not surpass N.

    Args:
    N (int): The maximum perimeter of the triangles.

    Returns:
    int: The number of primitive triangles with integer sides.
    """
    N //= 2
    res = 0
    for m in range(2, int(N**0.5) + 1):
        if m % 2 == 0:
            start = 1
        else:
            start = 2
        for n in range(start, min(m, N // m + 1), 2):
            if gcd(m, n) == 1:
                res += min(m, (N - m * n) // n + 1) - (n + 1) // 2
    return res

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)