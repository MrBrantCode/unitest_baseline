"""
QUESTION:
Create a function `sum_of_squares_even(n)` that takes an integer `n` as input and returns the sum of squares of all the even numbers from 0 up to `n`. The function should iterate through numbers from 0 to `n` (inclusive) and only consider even numbers for the sum of squares calculation.
"""

def sum_of_squares_even(n):
    sum = 0
    for i in range(n+1):
        if i % 2 == 0:
            sum += i**2
    return sum