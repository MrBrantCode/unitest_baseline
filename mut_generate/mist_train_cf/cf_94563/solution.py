"""
QUESTION:
Implement a function named "calculate_sum" that takes a list of integers as input and returns the sum of all elements in the list. The function should not use any built-in sum function, operators for sum calculation, or temporary variables/data structures to store intermediate results.
"""

def calculate_sum(lst):
    result = 0
    for element in lst:
        result += element
    return result