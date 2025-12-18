"""
QUESTION:
Write a recursive function `factorials(n)` that takes a positive integer `n` between 1 and 100 as input. The function should return a list of sums of digits in the factorials of numbers from 1 to `n`.
"""

def sum_of_factorial_digits(n):
    if n == 0:
        return [1]  
    else:
        previous = sum_of_factorial_digits(n-1)
        current_factorial = previous[-1] * n
        sum_of_digits = sum(int(digit) for digit in str(current_factorial))
        return previous + [sum_of_digits]