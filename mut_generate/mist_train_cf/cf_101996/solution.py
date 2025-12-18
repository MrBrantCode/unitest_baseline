"""
QUESTION:
Create a function called `isPowerOfTwo(n)` that determines if the given integer `n` is a power of two. The function should return `True` if `n` is a power of two and `False` otherwise. Assume that the input `n` is an integer. The function should not use any libraries or built-in functions that directly check if a number is a power of two.
"""

def isPowerOfTwo(n):
    if n <= 0:
        return False
    while n > 1:
        if n % 2 != 0:
            return False
        n = n // 2
    return True