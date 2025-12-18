"""
QUESTION:
Write a function named `sum_of_squares` that takes two parameters, `start` and `end`, representing a range of numbers. The function should return the sum of the squares of all numbers between `start` and `end` (inclusive). The `start` parameter must be less than or equal to the `end` parameter; if not, the function should return an error message stating that the `start` parameter should be less than the `end` parameter.
"""

def sum_of_squares(start, end):
    if start > end:
        return "Error: The start parameter should be less than the end parameter."
    
    sum = 0
    for num in range(start, end+1):
        sum += num**2
    
    return sum