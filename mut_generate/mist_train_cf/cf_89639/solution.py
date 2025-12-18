"""
QUESTION:
Create a function named `compute_sum_of_squares(n)` that calculates the sum of squares of all even numbers from 0 up to a given positive integer `n`. The function should use a single loop to identify the even numbers and calculate their sum of squares.
"""

def compute_sum_of_squares(n):
    sum = 0
    for i in range(n+1):
        if i % 2 == 0:
            sum += i ** 2
    return sum