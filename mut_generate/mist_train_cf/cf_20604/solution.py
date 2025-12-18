"""
QUESTION:
Write a function called `roman_to_decimal_and_sum` that takes two Roman numerals as input, converts them to decimal numbers, and returns their sum. The input Roman numerals should be validated to ensure they are valid. If either input is not a valid Roman numeral, the function should print an error message and return.
"""

import re

def roman_to_decimal_and_sum(roman1, roman2):
    """
    This function takes two Roman numerals as input, converts them to decimal numbers, 
    and returns their sum. The input Roman numerals are validated to ensure they are valid.

    Args:
        roman1 (str): The first Roman numeral.
        roman2 (str): The second Roman numeral.

    Returns:
        int or None: The sum of the two Roman numerals as a decimal number, or None if either input is not a valid Roman numeral.
    """

    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def roman_to_decimal(roman):
        decimal = 0
        prev_value = 0

        for char in reversed(roman):
            if char not in roman_map:
                return None
            curr_value = roman_map[char]
            if curr_value >= prev_value:
                decimal += curr_value
            else:
                decimal -= curr_value
            prev_value = curr_value

        return decimal

    # Validate input Roman numerals
    if not re.match(r'^[IVXLCDM]+$', roman1) or not re.match(r'^[IVXLCDM]+$', roman2):
        print("Invalid Roman numeral.")
        return

    decimal1 = roman_to_decimal(roman1)
    decimal2 = roman_to_decimal(roman2)

    if decimal1 is None or decimal2 is None:
        print("Invalid Roman numeral.")
        return

    return decimal1 + decimal2