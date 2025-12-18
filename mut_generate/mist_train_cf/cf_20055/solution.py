"""
QUESTION:
Design a function named `sum_of_cubes` that takes a parameter, which can be a positive integer or a string representing a positive integer. The function should calculate and return the sum of the cubes of the digits of the input number. If the input is not a valid positive integer or string representation of a positive integer, the function should return an error message.
"""

def sum_of_cubes(parameter):
    if isinstance(parameter, int) or isinstance(parameter, float):
        # Convert the parameter to a string
        parameter = str(parameter)
    elif not isinstance(parameter, str):
        return "Error: Invalid parameter"

    # Remove any leading or trailing whitespaces
    parameter = parameter.strip()

    # Check if the parameter is a valid positive integer
    if not parameter.isdigit() or int(parameter) <= 0:
        return "Error: Invalid parameter"

    # Calculate the sum of cubes of digits
    result = sum(int(digit) ** 3 for digit in parameter)

    return result