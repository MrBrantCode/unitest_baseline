"""
QUESTION:
Create a function named `decimal_to_hex` that takes one argument: `decimal_number`. The function should convert a non-negative integer `decimal_number` into its corresponding hexadecimal notation and return it as a string. The function should not include the '0x' prefix in the hexadecimal notation. If the input is not a non-negative integer, the function should return the error message "Invalid input. The number must be a non-negative integer."
"""

def decimal_to_hex(decimal_number):
    if isinstance(decimal_number, int) and decimal_number >= 0:
        return hex(decimal_number)[2:]
    else:
        return "Invalid input. The number must be a non-negative integer."