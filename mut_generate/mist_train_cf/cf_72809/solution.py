"""
QUESTION:
Create a function named `sum_squares_divisible_by_3` that takes a list of integers or a nested list of unknown depth as input. The function should return the sum of the squares of the numbers in the list that are divisible by 3.
"""

def sum_squares_divisible_by_3(lst):
    sum = 0
    for i in lst:
        if isinstance(i, list):
            sum += sum_squares_divisible_by_3(i)
        elif i % 3 == 0:
            sum += i**2
    return sum