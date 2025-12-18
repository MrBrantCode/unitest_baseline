"""
QUESTION:
Write a function `reverse_order(n)` that generates a list of numbers from `n` down to 1 in reverse order using recursion. The function should take an integer `n` as input and return a list of integers. For example, `reverse_order(10)` should return `[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]`.
"""

def reverse_order(n):
    if n == 1:
        return [1]
    else:
        return [n] + reverse_order(n-1)