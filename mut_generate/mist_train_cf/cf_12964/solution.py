"""
QUESTION:
Write a function `convert_base(number, current_base, target_base)` that takes a string representation of a non-negative integer `number`, its current base `current_base`, and a target base `target_base`, and returns the string representation of `number` converted to `target_base`. The current base and target base should be integers greater than 1 and less than or equal to 10.
"""

def convert_base(number, current_base, target_base):
    decimal_number = int(number, current_base)
    converted_number = ""
    while decimal_number > 0:
        remainder = decimal_number % target_base
        converted_number = str(remainder) + converted_number
        decimal_number = decimal_number // target_base
    return converted_number