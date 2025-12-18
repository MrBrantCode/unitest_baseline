"""
QUESTION:
Write a function `cumulative_harmonic_total` that calculates the cumulative total of the harmonic sequence from 1/1 to 1/N. The function should take an integer `N` as input and return the cumulative total.
"""

def cumulative_harmonic_total(N):
    total = 0.0
    for i in range(1, N + 1):
        total += 1 / i
    return total