"""
QUESTION:
Write a function `is_valid_decimal` that checks if a given string represents a valid decimal number. The function should return True if the string is a valid decimal number and False otherwise. A valid decimal number can be positive or negative (indicated by "+" or "-" respectively), can have one decimal point, and can have leading zeroes. However, it should not have more than one decimal point or any spaces, and should not be formatted improperly.
"""

def is_valid_decimal(s):
    """
    Checks if a given string represents a valid decimal number.

    A valid decimal number can be positive or negative (indicated by "+" or "-" respectively),
    can have one decimal point, and can have leading zeroes. However, it should not have more
    than one decimal point or any spaces, and should not be formatted improperly.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a valid decimal number, False otherwise.
    """

    # Remove leading and trailing whitespace
    s = s.strip()

    # Check for negative numbers
    if s.startswith('-'):
        # Remove the negative sign and check the rest of the string
        s = s[1:]
    elif s.startswith('+'):
        # Remove the positive sign and check the rest of the string
        s = s[1:]

    # Split the string into parts separated by the decimal point
    parts = s.split('.')

    # Check if there is more than one decimal point
    if len(parts) > 2:
        return False

    # Check if the decimal point is at the start of the string
    if len(parts[0]) == 0 and len(parts) == 2:
        return False

    # Check each part to ensure it is a valid integer
    for part in parts:
        # Check if the part is empty
        if len(part) == 0:
            continue
        # Check if the part contains any non-digit characters
        if not part.isdigit():
            return False

    # If all checks pass, the string is a valid decimal number
    return True