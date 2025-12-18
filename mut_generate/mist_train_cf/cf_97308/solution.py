"""
QUESTION:
Convert the character stream into a number by extracting and summing all valid numbers separated by non-numeric characters. The function should handle erroneous characters and negative numbers correctly. Implement a function `convert_char_stream(char_stream)` that takes a string `char_stream` as input and returns the sum of the extracted numbers. The input string may contain multiple numbers, non-numeric characters, and negative numbers.
"""

import re

def convert_char_stream(char_stream):
    numbers = re.findall(r'-?\d+', char_stream)  # Extract all numbers from the character stream
    return sum(int(number) for number in numbers)  # Convert the numbers to integers and sum them