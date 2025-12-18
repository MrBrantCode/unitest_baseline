"""
QUESTION:
Write a function `isPowerOfTwo(n: int)` that takes an integer `n` as input and returns a boolean value indicating whether `n` is a power of two. The function should return `False` for negative numbers and zero.
"""

def isPowerOfTwo(n: int) -> bool:
    if n <= 0:
        return False
    while n > 1:
        if n % 2 != 0:
            return False
        n //= 2
    return True