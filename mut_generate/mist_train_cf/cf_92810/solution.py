"""
QUESTION:
Write a function `sum_recursive` that calculates the sum of the first `n` positive integers using a recursive approach and displays the numbers in reverse order. The function should take an integer `n` as input and return the sum.
"""

def sum_recursive(n):
    if n == 1:
        print(n)
        return 1
    else:
        print(n)
        return n + sum_recursive(n-1)