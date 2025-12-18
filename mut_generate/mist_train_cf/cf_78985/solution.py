"""
QUESTION:
Design a function named `extract_and_sum` that takes a string as input, extracts all numeric characters from the string, converts them into integers, and returns these integers as a list along with their sum. The function should be able to handle strings with conjoined or hidden numbers.
"""

import re

def extract_and_sum(string):
    numbers = re.findall('\d+', string)
    int_numbers = [int(num) for num in numbers]
    return int_numbers, sum(int_numbers)