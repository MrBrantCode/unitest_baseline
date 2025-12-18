"""
QUESTION:
Compose a function called `is_credit_card_valid` that verifies whether a given string is a valid credit card number. The function should first check if the string comprises solely of numerical digits and has a length of 13 to 16 digits. Then, it should apply the Luhn algorithm to validate the string as a credit card number. The Luhn algorithm is a simple checksum formula used to validate identification numbers, where the sum of the digits at even indices (0-based indexing) are doubled and subtracted by 9 if the result is greater than 9, then the total sum of all digits is checked to be divisible by 10. If both conditions are met, the function should return True, otherwise False.
"""

import re

def is_credit_card_valid(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    if not re.match(r"^\d{13,16}$", card_number):
        return False
    sums = 0
    num_digits = len(card_number)
    parity = num_digits % 2
    for i in range(num_digits):
        digit = int(card_number[i])
        if i % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        sums += digit
    return sums % 10 == 0