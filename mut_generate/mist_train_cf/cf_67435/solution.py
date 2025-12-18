"""
QUESTION:
Write a function named `is_valid_decimal` that takes a string as input and returns `True` if the string represents a decimal number with a precision of 2, and `False` otherwise. The input string must meet the following conditions: it is a positive number, falls within the range (0, 1000), is not a multiple of 10, and may contain leading and/or trailing whitespaces.
"""

def is_valid_decimal(s):
    stripped_str = s.strip()
    try:
        number = float(stripped_str)
        if (str(number) == stripped_str) and (int(stripped_str) != int(number)):
            fract_part = int(str(number).split('.')[1])
            if 0 < number < 1000 and number % 10 != 0 and len(str(fract_part)) == 2:
                return True
        return False
    except ValueError:
        return False