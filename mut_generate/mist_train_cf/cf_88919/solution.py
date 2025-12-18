"""
QUESTION:
Design a function named `sum_of_digit_cubes` that calculates the sum of the cubes of the digits of a given input. The input can be a single positive integer or string representing a positive integer, or a list of integers or strings. If the input is not a valid positive integer or string representation of a positive integer, the function should return an error message. The function should have a time complexity of O(n), where n is the number of digits in the input parameter.
"""

def sum_of_digit_cubes(n):
    if isinstance(n, list):
        sum_of_cubes = 0
        for element in n:
            sum_of_cubes += sum_of_digit_cubes(element)
        return sum_of_cubes
    elif isinstance(n, int):
        n = str(n)
    elif not isinstance(n, str):
        return "Error: Invalid parameter"

    sum_of_cubes = 0

    for digit in n:
        if digit.isdigit():
            sum_of_cubes += int(digit) ** 3

    return sum_of_cubes