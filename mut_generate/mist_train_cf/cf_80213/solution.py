"""
QUESTION:
Write a function `solve(n)` that calculates the sum of the lengths of the recurring cycles of the decimal representations of unit fractions with prime denominators from 3 to `n`. The length of the recurring cycle of a unit fraction with denominator `p` is defined as the smallest positive integer `x` such that `10^x mod p` equals 1. The function should return the sum of these lengths for all prime denominators from 3 to `n`. Note that the function should only consider denominators with prime factors other than 2 and/or 5.
"""

def cycle_length(p):
    x = 1
    while pow(10, x, p) != 1:
        x += 1
    return x


def solve(n):
    sieve = [0, 0] + [1 for _ in range(2, n)]
    sum_cycle_len = 0

    for x in range(2, n):
        if sieve[x] == 1 and (x % 2 != 0 and x % 5 != 0):
            sum_cycle_len += cycle_length(x)
            for y in range(2*x, n, x):
                sieve[y] = 0

    return sum_cycle_len