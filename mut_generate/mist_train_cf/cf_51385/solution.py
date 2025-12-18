"""
QUESTION:
Write a function named `is_credit_card_valid` that takes a credit card number as input and returns `True` if the card number is valid according to the Luhn algorithm, and `False` otherwise. The function should only validate the card number's integrity using the Luhn algorithm, without considering other factors such as expiration dates, account balances, or security codes. The input credit card number should be a string of digits between 13 to 19 characters long.
"""

def is_credit_card_valid(card_number):
    """
    Validate a credit card number using the Luhn algorithm.

    Args:
        card_number (str): A string of digits representing the credit card number.

    Returns:
        bool: True if the card number is valid, False otherwise.
    """

    # Check if the number contains only digits and has a length between 13 to 19 digits
    if not card_number.isdigit() or not 13 <= len(card_number) <= 19:
        return False

    # Reverse the credit card number
    reversed_card_number = card_number[::-1]

    # Initialize sum to 0
    total_sum = 0

    # Iterate over the reversed credit card number
    for i, digit in enumerate(reversed_card_number):
        # Convert the digit to an integer
        digit = int(digit)

        # If i is even, add the digit to sum
        if i % 2 == 0:
            total_sum += digit
        # If i is odd, multiply the digit by 2 and add the result to sum
        else:
            doubled_digit = digit * 2
            # If the result is a two digit number, add the digits of the result together
            if doubled_digit > 9:
                doubled_digit = (doubled_digit // 10) + (doubled_digit % 10)
            total_sum += doubled_digit

    # If sum modulo 10 is 0, the credit card number is valid
    return total_sum % 10 == 0