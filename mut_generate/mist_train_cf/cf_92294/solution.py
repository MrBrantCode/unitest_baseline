"""
QUESTION:
Create a function `convert_number_to_string(number, base)` that converts a positive number to its string representation in a given base, where the base is between 2 and 16 (inclusive). The function should return the result as a string.
"""

def convert_number_to_string(number, base):
    if number == 0:
        return ''

    remainder = number % base
    if remainder < 10:
        digit = str(remainder)
    else:
        digit = chr(ord('A') + remainder - 10)

    return convert_number_to_string(number // base, base) + digit