"""
QUESTION:
Implement a function called `validate_credit_card` to determine whether a given credit card number is valid using the Luhn algorithm. The function should accept a string of digits as input and return a boolean indicating whether the credit card number is valid.
"""

def validate_credit_card(card_number):
    """
    Validates a credit card number using the Luhn algorithm.

    Args:
        card_number (str): A string of digits representing the credit card number.

    Returns:
        bool: True if the credit card number is valid, False otherwise.
    """

    # Convert the card number to a list of integers
    digits = [int(x) for x in card_number]

    # Reverse the list of digits
    digits = digits[::-1]

    # Double every second digit
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        # Subtract 9 from numbers over 9
        if digits[i] > 9:
            digits[i] -= 9

    # If the sum is divisible by 10, the number is valid
    return sum(digits) % 10 == 0