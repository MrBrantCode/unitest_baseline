"""
QUESTION:
Write a function `sum_of_numbers` that takes a string of numbers separated by commas and returns the sum of all the numbers in the string. The string may contain negative numbers, floating-point numbers, spaces, and parentheses. It may also contain invalid characters, which should be ignored.
"""

import re

def sum_of_numbers(string):
    # Remove any non-numeric characters
    string = re.sub(r'[^0-9.,-]', '', string)
    
    # Split the string into individual numbers
    numbers = re.split(r'[, ]+', string)
    
    # Convert the numbers to floats and sum them up
    total = 0
    for number in numbers:
        try:
            total += float(number)
        except ValueError:
            pass
    
    return total