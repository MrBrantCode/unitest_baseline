"""
QUESTION:
Write a function `fast_algo(n)` that calculates the sum of all numbers from 0 to n. The function should have a time complexity of O(1) and return an integer result. The input `n` is a non-negative integer.
"""

def fast_algo(n):
    return (n * (n + 1)) // 2