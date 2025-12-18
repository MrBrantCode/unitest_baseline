"""
QUESTION:
Write a function `fast_algo(n)` that calculates the sum of all integers from 0 up to (but not including) a given number n. The solution should have a time complexity of O(1), meaning it must be constant time regardless of the size of n.
"""

def fast_algo(n):
    return n * (n - 1) // 2