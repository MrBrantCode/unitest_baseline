"""
QUESTION:
Write a recursive function `calc_sum_and_factorial(n)` that calculates the sum of the factorials of all positive integers from 1 to `n`, where `n` is a given positive integer. The function should not use any built-in functions for calculating factorials.
"""

def calc_sum_and_factorial(n):
    if n == 0:
        return 0
    else:
        fact = 1
        for i in range(1,n+1):
            fact *= i
        return fact + calc_sum_and_factorial(n-1)