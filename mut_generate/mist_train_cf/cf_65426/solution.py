"""
QUESTION:
Create a function `sum_even_squares(n)` that calculates the sum of squares of even numbers from 0 up to `n`. The function should consider the absolute value of `n` if it is negative. Return the sum as an integer.
"""

def sum_even_squares(n: int) -> int:
    n = abs(n)
    return sum(num**2 for num in range(0, n+1, 2))