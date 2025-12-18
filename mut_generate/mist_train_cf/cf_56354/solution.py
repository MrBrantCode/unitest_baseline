"""
QUESTION:
Implement a function named `verify_checksum` that takes a 13-digit string `ean` as input and returns a boolean indicating whether the EAN-13 code's checksum is valid. The checksum is calculated by alternately adding and multiplying by 3 the first 12 digits of the code, then comparing the last digit of this total with the 13th digit of the code.
"""

def verify_checksum(ean):
    """
    Verifies the checksum of a given EAN-13 code.

    Args:
        ean (str): A 13-digit EAN code.

    Returns:
        bool: True if the checksum is valid, False otherwise.
    """
    total = 0
    for i in range(12):
        if i % 2 == 0:
            total += int(ean[i])
        else:
            total += int(ean[i]) * 3
    check_digit = (10 - (total % 10)) % 10
    return check_digit == int(ean[-1])