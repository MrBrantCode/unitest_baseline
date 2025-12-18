"""
QUESTION:
Implement a function called `calculate_sum` that takes a list of numbers as input and returns the sum of all elements in the list. The function should not use any built-in functions or operators for calculating the sum, and it should not use any temporary variables or data structures to store intermediate results during the calculation.
"""

def calculate_sum(numbers):
    result = 0
    for num in numbers:
        result += num
    return result