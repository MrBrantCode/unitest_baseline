"""
QUESTION:
Implement a function named `calculate_sum` that takes a list of integers as input and returns the sum of all elements without using any built-in functions or operators for calculating the sum. The function should not use temporary variables or data structures to store intermediate results.
"""

def calculate_sum(lst):
    result = 0
    for num in lst:
        result += num
    return result