"""
QUESTION:
Write a function `check_number_type` that takes a single argument and returns a string indicating whether the input is an even number, an odd number, a decimal number, or an invalid number. The function should handle both positive and negative inputs, and should raise an exception or return an error message if the input is not a valid number.
"""

def check_number_type(number):
    try:
        number = float(number)
        if number.is_integer():
            if number % 2 == 0:
                return "Even"
            else:
                return "Odd"
        else:
            return "Decimal"
    except ValueError:
        return "Invalid number"