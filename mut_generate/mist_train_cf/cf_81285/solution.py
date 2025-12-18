"""
QUESTION:
Write a function `count_series(total)` that determines the number of possible arithmetic series consisting of sequential odd integers that sum up to the given `total`. The function should return the count of such series.

The arithmetic series can start from any odd integer `a` and has a common difference `d` of 2. The cumulative total `S` of the series can be calculated by the formula: `S = n/2 * (2a + (n-1)d)`, where `n` is the number of terms in the series.

The function should find all integer solutions of `n` for each odd integer `a` within range, where `n` is a positive integer.
"""

def count_series(total):
    count = 0
    a = 1
    while True:
        n = (2*total) / (2*a + 2*(a-1))
        if n < 1:
            break
        if n == int(n):
            count += 1
        a += 2
    return count