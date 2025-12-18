"""
QUESTION:
Write a function `recursive_sum(n)` that calculates the sum of all natural numbers from 0 to n using recursion. The function should have a time complexity of O(n), and it should not use any built-in sum() or range() functions. The input n should be a non-negative integer.
"""

def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n-1)