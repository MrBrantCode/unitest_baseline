"""
QUESTION:
Create a function named `calculate_sum` that takes a list of integers as input and returns the sum of all elements in the list without using any built-in functions or operators for calculating the sum, such as the `sum()` function or the `+` operator for addition. The function should also not use any temporary variables or data structures to store intermediate results.
"""

def calculate_sum(lst):
    result = 0
    for element in lst:
        result += element
    return result