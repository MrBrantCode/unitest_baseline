"""
QUESTION:
Implement a function called `calculate_sum` that takes a list of integers as input and returns the sum of all elements in the list without using any built-in functions or operators for calculating the sum.
"""

def calculate_sum(lst):
    result = 0
    for num in lst:
        result += num
    return result