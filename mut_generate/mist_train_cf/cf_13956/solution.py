"""
QUESTION:
Write a function named `sum_multiples_3_5` that takes a positive integer `n` (less than or equal to 100) as input and returns the sum of all the multiples of 3 and 5 between 0 and `n`, using recursion.
"""

def sum_multiples_3_5(n):
    if n <= 0:
        return 0
    elif n % 3 == 0 or n % 5 == 0:
        return n + sum_multiples_3_5(n-1)
    else:
        return sum_multiples_3_5(n-1)