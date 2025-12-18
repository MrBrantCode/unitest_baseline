"""
QUESTION:
Create a function named `format_numbers` that takes a list of numbers as input and returns a list of strings where each number is rounded to the nearest hundredth decimal place and formatted with commas as thousands separators. The input list is assumed to only contain numeric values.
"""

def format_numbers(numbers):
    return ["{:,.2f}".format(round(number, 2)) for number in numbers]