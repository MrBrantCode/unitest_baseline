"""
QUESTION:
Write a recursive function named `convert_number_to_string` that takes a positive number and a base between 2 and 16 as parameters, and returns the string representation of the number in the given base. The function should handle digits greater than 9 using uppercase letters (A-F for 10-15).
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