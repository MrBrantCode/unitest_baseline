"""
QUESTION:
Write a Python function named `calculate_cube_volume` that takes an array of three side lengths as input and returns the volume of the cube. The input array must contain exactly three positive integers. If the input array does not meet this requirement, the function should return an error message. The function should also handle cases where the input array contains negative integers or non-numeric values and return an error message in these cases. Additionally, the function should either round floating-point numbers to the nearest integer or return an error message indicating that floating-point numbers are not allowed. The function should use a custom mathematical function to calculate the volume of the cube, which should take the side lengths as input and return the volume as output.
"""

def calculate_cube_volume(side_lengths):
    # Validate input array
    if len(side_lengths) != 3:
        return "Input array must contain exactly three positive integers"

    # Validate side lengths
    for length in side_lengths:
        if not isinstance(length, int) or length <= 0:
            return "Side lengths must be positive integers"

    # Convert floating-point numbers to integers
    side_lengths = [int(length) for length in side_lengths]

    # Calculate volume using custom mathematical function
    volume = custom_multiply(*side_lengths)

    return volume


def custom_multiply(*args):
    # Implement custom mathematical function to calculate volume of cube
    result = 1
    for arg in args:
        result *= arg
    return result