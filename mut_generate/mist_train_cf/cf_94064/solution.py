"""
QUESTION:
Write a function `validate_credit_card_number(card_number)` that validates a given credit card number and returns a tuple containing a boolean indicating whether the card number is valid and the type of the credit card. The function should validate the card number using the Luhn algorithm and check the card number prefix and length for each type. The card types and their corresponding prefixes and lengths are as follows:

- Visa: starts with 4 and has a length of 16 digits
- MasterCard: starts with 51, 52, 53, 54, or 55 and has a length of 16 digits
- American Express: starts with 34 or 37 and has a length of 15 digits
- Discover: starts with 6011 and has a length of 16 digits

The function should not rely on any external libraries or modules and should return False if the card number is invalid.
"""

def validate_credit_card_number(card_number):
    # Remove any spaces or dashes from the card number
    card_number = card_number.replace(' ', '').replace('-', '')

    # Check the length of the card number
    if len(card_number) not in [15, 16]:
        return False, None

    # Check the card number prefix and length for each type
    if card_number[0] == '4' and len(card_number) == 16:
        card_type = 'Visa'
    elif card_number[:2] in ['51', '52', '53', '54', '55'] and len(card_number) == 16:
        card_type = 'MasterCard'
    elif card_number[:2] in ['34', '37'] and len(card_number) == 15:
        card_type = 'American Express'
    elif card_number[:4] == '6011' and len(card_number) == 16:
        card_type = 'Discover'
    else:
        return False, None

    # Apply the Luhn algorithm to validate the card number
    checksum = 0
    is_second_digit = False
    for digit in card_number[::-1]:
        digit = int(digit)
        if is_second_digit:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
        is_second_digit = not is_second_digit

    return checksum % 10 == 0, card_type