"""
QUESTION:
Create a function named `check_numbers` that takes an input string containing multiple lines of numbers. The function should return a list of numbers that start with the integer 8, have a length of exactly 6 digits, and are divisible by 3.
"""

import re

def check_numbers(input_str):
    pattern = r'^8\d{5}$'
    result_list = re.findall(pattern, input_str, re.MULTILINE)
    divisible_by_3 = [int(num) for num in result_list if int(num) % 3 == 0]
    return divisible_by_3