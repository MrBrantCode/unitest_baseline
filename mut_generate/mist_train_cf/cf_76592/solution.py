"""
QUESTION:
Extract all numerical values from a given input string. The function should be able to handle negative numbers, decimal numbers, irregular spacing, and numbers embedded within words. It should also handle any exceptions that may occur.

The function name should be `extract_numbers` and it should take one parameter `input_str`. The function should return a list of extracted numbers, which can be either integers or floats.
"""

import re

def extract_numbers(input_str):
    try:
        # Regex to match decimal and negative numbers:
        # \b start of the digit
        # -? optional negative symbol
        # \d* zero or more digits before the decimal point
        # \.? optional decimal point
        # \d+ at least one digit after the decimal point
        # \b end of the digit
        values = re.findall(r'\b-?\d*\.?\d+\b', input_str)
        return [float(val) if '.' in val else int(val) for val in values]
    except Exception as ex:
        print(f"An error occurred: {ex}")