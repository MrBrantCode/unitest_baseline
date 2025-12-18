"""
QUESTION:
Write a function named `convert_char_stream` that takes a string of characters as input and returns the sum of all valid numbers found in the string. The input string may contain non-numeric characters, multiple numbers separated by non-numeric characters, and negative numbers.
"""

import re

def convert_char_stream(char_stream):
    numbers = re.findall(r'-?\d+', char_stream)  
    return sum(int(number) for number in numbers)  