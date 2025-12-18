"""
QUESTION:
Create a Python function `calculate_disparity` that takes two distinct integer values as inputs and returns the result of the following multi-step mathematical operations: calculate the absolute difference between the two values, square the absolute difference, add the original values to the squared difference, and subtract 5 from the result. The function should also return an error message if the inputs are not integers or are not distinct.
"""

def calculate_disparity(value1, value2):
    if type(value1) != int or type(value2) != int:
        return "Invalid input! Only integer values are accepted."

    if value1 == value2:
        return "Invalid input! Provide two distinct integer values."

    absolute_difference = abs(value1 - value2)
    square_difference = absolute_difference ** 2
    final_result = square_difference + value1 + value2
    final_result -= 5

    return final_result