"""
QUESTION:
Write a function `sum_numbers(n)` that calculates the sum of numbers between 1 and `n` (inclusive) using recursion, excluding any number that is divisible by 3. The function should return 0 when `n` is less than or equal to 0.
"""

def sum_numbers(n):
    if n <= 0:  
        return 0
    elif n % 3 == 0:  
        return sum_numbers(n-1)
    else:
        return n + sum_numbers(n-1)  