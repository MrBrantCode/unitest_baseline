"""
QUESTION:
Write a function `extract_numbers(input_str)` that takes a string `input_str` as input and returns a list of floats representing the numbers extracted from the string. The function should extract numbers that may contain a decimal point, ignore commas and other non-numeric characters, and assume the input string contains no negative numbers.
"""

import re

def extract_numbers(input_str):
    num_list = re.findall(r'\d+\.\d+|\d+', input_str)  # Using regular expression to find numbers with or without decimal points
    num_float_list = [float(num) for num in num_list]  # Converting the extracted numbers to floats
    return num_float_list