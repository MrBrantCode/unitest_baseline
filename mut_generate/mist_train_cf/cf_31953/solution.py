"""
QUESTION:
Write a function `rabbit_pairs(n, k)` that takes in two positive integers, n and k, and returns the total number of rabbit pairs present after n months, where each pair of rabbits produces k offspring every month. The initial population consists of a single pair of rabbits. The function should handle cases where n is greater than 2.
"""

def rabbit_pairs(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return rabbit_pairs(n-2, k) * k + rabbit_pairs(n-1, k)