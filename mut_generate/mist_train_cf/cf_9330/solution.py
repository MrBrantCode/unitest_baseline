"""
QUESTION:
Write a function `check_number_type(number)` that takes a number as input and returns whether it's "Even", "Odd", "Decimal", or "Invalid number". The function should be able to handle both positive and negative numbers, as well as decimal numbers. If the input cannot be converted to a number, it should return "Invalid number".
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