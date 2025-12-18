"""
QUESTION:
Design a function named `calculate_factorial` that takes a tuple of integers and a list as input, calculates the factorial of each non-negative integer in the tuple, and appends the results to the given list. The function should handle tuples containing zero and negative numbers by appending an error message for each negative number, and return an error message if the input tuple is empty.
"""

import math

def calculate_factorial(tup, result_list):
    if not tup:
        return "Error: Tuple is empty"
    else:
        for num in tup:
            if num >= 0:
                fact = math.factorial(num)
                result_list.append(fact)
            else:
                result_list.append('Error: Factorial not defined for negative numbers')
    return result_list