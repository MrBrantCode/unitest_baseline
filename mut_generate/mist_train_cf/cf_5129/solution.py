"""
QUESTION:
Create a recursive function called `recursive_function` that takes three parameters: a number (which can be positive or negative), a base (which can be any positive integer), and a precision value (which indicates the number of decimal places to include in the result). The function should return the result as a string. The function should also handle error cases such as invalid inputs, division by zero, or other potential errors. The base and precision should be integers, and the base should be positive while the precision should be non-negative.
"""

def recursive_function(number, base, precision):
    # Error handling for invalid inputs
    if not isinstance(number, (int, float)) or not isinstance(base, int) or not isinstance(precision, int):
        return "Invalid input. Please provide a number, base, and precision as integers or floats."
    if base <= 0 or precision < 0:
        return "Invalid input. Base should be a positive integer and precision should be a non-negative integer."

    # Base case: precision is 0
    if precision == 0:
        return str(round(number))

    # Recursive case
    integer_part = int(number)
    fractional_part = abs(number - integer_part)
    result = str(integer_part) + "."

    if fractional_part > 0:
        # Multiply the fractional part by the base to get the next digit
        next_digit = int(fractional_part * base)
        result += str(next_digit)

        # Subtract the rounded value of the next digit from the fractional part
        fractional_part -= next_digit / base

        # Recursive call to calculate the next digit
        next_digits = recursive_function(fractional_part, base, precision - 1)
        result += next_digits

    # Return the result as a string
    return result