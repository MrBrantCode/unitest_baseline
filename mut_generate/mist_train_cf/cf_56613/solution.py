"""
QUESTION:
Write a function `count_trailing_zeros_factorial(n)` that calculates the number of trailing zeros in the binary representation of `n` factorial. The function should take an integer `n` as input and return the count of trailing zeros. Note that this is equivalent to counting the number of times 2 divides `n` factorial without a remainder.
"""

def count_trailing_zeros_factorial(n):
    cnt = 0
    i = 2
    while n / i >= 1:
        cnt += int(n / i)
        i *= 2
    return cnt