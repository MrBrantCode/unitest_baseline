"""
QUESTION:
Develop a function named `extract_even_numbers` that takes a string `s` as input and returns a list of integers representing the even numbers found in the string, in the order they appear. The string may contain alphanumeric characters, special characters, white spaces, and integers separated by various delimiters such as commas, semi-colons, spaces, pipes, and colons.
"""

import re

def extract_even_numbers(s):
    # Extract all numbers using regex
    numbers = re.findall(r'\b\d+\b', s)

    # Filter only even numbers and convert them into integers
    even_numbers = [int(num) for num in numbers if int(num) % 2 == 0]

    return even_numbers