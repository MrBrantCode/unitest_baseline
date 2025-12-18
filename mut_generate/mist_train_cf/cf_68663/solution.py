"""
QUESTION:
Implement a function `validate_card(card_number)` that takes a string of digits as input, representing a credit card number. The function should return a string indicating the type of credit card (Visa, MasterCard, American Express, Discover) if the number is valid, or an error message if the number is invalid. 

A valid credit card number should meet the following conditions:
- It should only contain numeric characters.
- It should be between 13 and 19 digits long.
- It should pass the Luhn algorithm check.

The function should identify the type of credit card based on the following patterns:
- American Express: starts with 34 or 37
- MasterCard: starts with a number between 51 and 55
- Visa: starts with 4
- Discover: starts with 6011, 65, or a number between 622126 and 622925, or a number between 644 and 649. 

Return the card type followed by ' card is valid.' for valid numbers, or an error message for invalid numbers.
"""

def validate_card(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    
    def luhn_check(card_number):
        nums = digits_of(card_number)
        check_sum = sum(nums[::-2] + [sum(divmod(d * 2, 10)) for d in nums[-2::-2]])
        return check_sum % 10 == 0

    if not card_number.isdigit(): 
        return 'Invalid input. Non-numeric characters are not allowed.'
    elif not (len(card_number) >= 13 and len(card_number) <= 19):
        return 'Invalid card number length. It must be between 13 and 19 digits.'
    elif not luhn_check(card_number):
        return 'Invalid card number.'
    else:
        if card_number[0:2] in ['34', '37']: 
            return 'American Express card is valid.'
        elif int(card_number[0:2]) in range(51,56): 
            return 'MasterCard card is valid.'
        elif card_number[0] in ['4']: 
            return 'Visa card is valid.'
        elif card_number[0:4] in ['6011'] or card_number[0:2] in ['65'] or int(card_number[0:6]) in range(622126, 622926) \
                or int(card_number[0:3]) in range(644,650): 
            return 'Discover card is valid.'
        else:
            return 'Unknown card type.'