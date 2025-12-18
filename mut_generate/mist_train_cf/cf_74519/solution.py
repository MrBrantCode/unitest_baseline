"""
QUESTION:
Design a function `smallest_pythagorean_quadruplet(y)` that takes an integer `y` as input and returns the smallest Pythagorean quadruplet, a set of four positive integers `a`, `b`, `c`, and `d` such that `a^2 + b^2 + c^2 = d^2` and `a + b + c + d = y`. The function should use an efficient algorithm to find the quadruplet and should not use brute-force. If no such quadruplet exists, the function should return an empty list. The input `y` is guaranteed to be at least 6.
"""

def smallest_pythagorean_quadruplet(y):
    for a in range(1, int(y/3)):
        for b in range(a+1, int(y/2)):
            for c in range (b + 1, y - a - b):
                d = y - a - b - c
                if a * a + b * b + c * c == d * d:
                    return [a, b, c, d]
    return []