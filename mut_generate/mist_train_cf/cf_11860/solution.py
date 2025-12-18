"""
QUESTION:
Write a function `sum_of_odd_numbers(start, end)` that uses recursion to calculate the sum of all odd numbers within the given range. The function should take two parameters, `start` and `end`, representing the start and end of the range respectively, and return the sum of all odd numbers within this range.
"""

def sum_of_odd_numbers(start, end):
    if start > end:
        return 0
    elif start % 2 == 1:
        return start + sum_of_odd_numbers(start+2, end)
    else:
        return sum_of_odd_numbers(start+1, end)