"""
QUESTION:
Create a function named `convert_to_integer` that takes a string as input, parses the string for numbers in various formats (including scientific notation, decimal numbers, and multiple numbers separated by commas), and returns a list of integers equivalent to the parsed numbers. The input string may contain leading or trailing spaces, numbers with different formats (e.g., "1.23E+10" or "1.23e+10"), negative numbers, and numbers with multiple decimal points or scientific notation formats. The function should handle extremely large or small numbers within the range of the integer data type.
"""

import re

def convert_to_integer(input_string):
    input_string = input_string.strip()
    numbers = input_string.split(",")
    result = []
    for number in numbers:
        number = number.replace(" ", "")
        match = re.match(r"([-+]?\d+(\.\d+)?([eE][-+]?\d+)?)", number)
        if match:
            number_str = match.group(1)
            number_int = int(float(number_str))
            result.append(number_int)
    return result