"""
QUESTION:
Write a function `extract_numbers` that takes a format string as input and returns a list of numbers. The format string may contain placeholders for integers (`%i`), floats (`%f`), and hexadecimal numbers (`%x`). The function should handle nested placeholders and prompt the user to input the corresponding values. The returned list should contain the input values in the order of their appearance in the format string.
"""

import re

def extract_numbers(format_string):
    # Define regular expressions for integer, float, and hexadecimal patterns
    int_pattern = r'%i'
    float_pattern = r'%f'
    hex_pattern = r'%x'
    
    # Find all integer, float, and hexadecimal patterns in the format string
    int_matches = re.findall(int_pattern, format_string)
    float_matches = re.findall(float_pattern, format_string)
    hex_matches = re.findall(hex_pattern, format_string)
    
    # Initialize an empty list to store the extracted numbers
    numbers = []
    
    # Extract integer values from the integer matches
    for match in int_matches:
        number = input(f"Enter an integer value for {match}: ")
        numbers.append(int(number))
    
    # Extract float values from the float matches
    for match in float_matches:
        number = input(f"Enter a float value for {match}: ")
        numbers.append(float(number))
    
    # Extract hexadecimal values from the hexadecimal matches
    for match in hex_matches:
        number = input(f"Enter a hexadecimal value for {match}: ")
        numbers.append(int(number, 16))
    
    # Return the list of extracted numbers
    return numbers