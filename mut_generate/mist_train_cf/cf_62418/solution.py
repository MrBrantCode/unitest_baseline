"""
QUESTION:
Write a function `find_trailing_zeros(n)` that calculates the number of trailing zeros in the result of `n!` (n factorial), where `n` is a positive integer. The function should only consider the factors of 5 in the factorial.
"""

def find_trailing_zeros(n):
    count = 0
    i = 5
    while (n / i>= 1):
        count += int(n / i)
        i *= 5
    return int(count)