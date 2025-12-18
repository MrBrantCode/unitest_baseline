"""
QUESTION:
Write a function `sum_of_cubes(parameter)` that calculates the sum of the cubes of the digits of a given number. The function should accept both integers and string representations of positive integers as input, and return an error message if the input is not a valid positive integer or string representation of a positive integer.
"""

def sum_of_cubes(parameter):
    if isinstance(parameter, int) or isinstance(parameter, float):
        parameter = str(parameter)
    elif not isinstance(parameter, str):
        return "Error: Invalid parameter"

    parameter = parameter.strip()

    if not parameter.isdigit():
        return "Error: Invalid parameter"

    result = sum(int(digit) ** 3 for digit in parameter)

    return result