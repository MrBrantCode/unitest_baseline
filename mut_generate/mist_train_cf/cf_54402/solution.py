"""
QUESTION:
Create a function `is_valid_num` that takes a string as input and returns a boolean. The function should verify that the string represents a decimal number with a maximum precision of four decimal places, is positive, and lies within the range of 0 to 10000, inclusive. The function should also support scientific notation.
"""

def is_valid_num(string):
    try:
        # Attempts to convert the string into a float.
        number = float(string)
    except ValueError:
        # If an error occurs during the conversion, that means the string does not represent a number.
        return False

    # Checks if the number is within the range.
    if number < 0 or number > 10000:
        return False

    # Attempts to find the number of digits after the decimal point. It also takes into consideration the scientific notation. e.g ('1.23e3', '2.123456e-3', '0.003e3')
    decimal_part = string.split('.')[-1].split('e')[0] if '.' in string else ''

    # Checks the precision.
    if len(decimal_part) > 4:
        return False

    # The string passes all checks.
    return True