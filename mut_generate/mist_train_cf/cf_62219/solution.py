"""
QUESTION:
Create a function called `isFibonacci` that takes an integer `n` as input and returns a boolean value indicating whether `n` is a Fibonacci number. The function should have a time complexity better than O(n) and should be able to handle large inputs efficiently.
"""

import math


def isFibonacci(n):
    def isPerfectSquare(x):
        s = int(math.sqrt(x))
        return s*s == x

    x = 5 * n * n + 4
    y = 5 * n * n - 4

    return isPerfectSquare(x) or isPerfectSquare(y)