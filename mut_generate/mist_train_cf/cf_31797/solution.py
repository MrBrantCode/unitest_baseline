"""
QUESTION:
Implement a function named `validate_credit_card` that takes two parameters: `card_number` (a string representing the credit card number) and `provider` (a string representing the credit card provider). The function should return `True` if the card number is valid according to the Luhn algorithm and matches the pattern of the specified provider, and `False` otherwise. The function should support the following providers: Mastercard, Visa, Discover, Diners Club, and JCB.
"""

import re

def validate_credit_card(card_number: str, provider: str) -> bool:
    def luhn_checksum(card_number):
        digits = [int(x) for x in card_number]
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        for digit in even_digits:
            checksum += sum(divmod(digit * 2, 10))
        return checksum % 10 == 0

    patterns = {
        'mastercard': r'^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$',
        'visa': r'^4[0-9]{12}([0-9]{3}){0,2}$',
        'discover': r'^6(?:011|5[0-9]{2})[0-9]{12}$',
        'diners_club': r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$',
        'jcb': r'^(?:2131|1800|35\d{3})\d{11}$'
    }
    pattern = patterns.get(provider.lower(), '')
    return luhn_checksum(card_number) and bool(re.match(pattern, card_number))