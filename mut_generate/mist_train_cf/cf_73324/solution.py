"""
QUESTION:
Create a function named `find_negative_numbers` that finds negative numbers of 2, 3, 4, and 5 digits in a given string. The numbers should be followed by a specific currency symbol (e.g., €, £, $). The function should return four regular expressions that match these numbers. The numbers have a comma as the decimal separator and two digits after the decimal point.
"""

import re

def find_negative_numbers(text, currency):
    """
    This function finds negative numbers of 2, 3, 4, and 5 digits in a given string.
    The numbers should be followed by a specific currency symbol.

    Parameters:
    text (str): The input string to search for negative numbers.
    currency (str): The currency symbol to match.

    Returns:
    list: A list of four regular expressions that match the negative numbers.
    """

    # Define the regular expressions for 2, 3, 4, and 5-digit negative numbers
    pattern_2_digit = re.compile(f"-\\d{{2}},\\d{{2}}{currency}")
    pattern_3_digit = re.compile(f"-\\d{{3}},\\d{{2}}{currency}")
    pattern_4_digit = re.compile(f"-\\d{{4}},\\d{{2}}{currency}")
    pattern_5_digit = re.compile(f"-\\d{{5}},\\d{{2}}{currency}")

    # Find all matches in the input text
    matches_2_digit = pattern_2_digit.findall(text)
    matches_3_digit = pattern_3_digit.findall(text)
    matches_4_digit = pattern_4_digit.findall(text)
    matches_5_digit = pattern_5_digit.findall(text)

    # Return the matches
    return [matches_2_digit, matches_3_digit, matches_4_digit, matches_5_digit]