"""
QUESTION:
Implement the `validate_ean13` function, which takes a 13-digit string as input and returns `True` if the string is a valid EAN-13 number according to the EAN-13 checksum algorithm, and `False` otherwise. The EAN-13 checksum algorithm works as follows: (1) from the rightmost digit, multiply every second digit by 3 and every other digit by 1, (2) sum the resulting numbers, and (3) check if the total sum is a multiple of 10. The input string must consist only of digits.
"""

def validate_ean13(ean):
    """
    Validate a 13-digit EAN number according to the EAN-13 checksum algorithm.

    Args:
        ean (str): A 13-digit string consisting only of digits.

    Returns:
        bool: True if the string is a valid EAN-13 number, False otherwise.
    """
    odd_sum = sum(int(x) for i, x in enumerate(reversed(ean)) if i % 2 == 0)
    even_sum = sum(int(x) for i, x in enumerate(reversed(ean)) if i % 2 == 1)
    total = (odd_sum + even_sum * 3)
    return total % 10 == 0