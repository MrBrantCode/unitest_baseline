"""
QUESTION:
Recognize the type of a credit card from a given string of numbers and validate the input string. The function should be named `recognize_credit_card` and should not use any built-in credit card validation libraries or functions. 

The function should check the following credit card types: 
- Visa cards start with 4 and have a length of either 13 or 16 digits.
- Mastercard cards start with 5 and have a length of 16 digits.
- American Express cards start with 3, followed by either 4 or 7, and have a length of 15 digits.

If the input string matches any of the criteria for the above credit card types, the function should return the corresponding card type (e.g. "Visa", "Mastercard", "American Express"). If the input string does not match any of the criteria or contains non-numeric characters, the function should return "Invalid input".
"""

def recognize_credit_card(card_number):
    if not card_number.isdigit():
        return "Invalid input"

    if len(card_number) == 13 or len(card_number) == 16:
        if card_number[0] == '4':
            return "Visa"
    elif len(card_number) == 16:
        if card_number[0] == '5':
            return "Mastercard"
    elif len(card_number) == 15:
        if card_number[0] == '3' and (card_number[1] == '4' or card_number[1] == '7'):
            return "American Express"
    
    return "Invalid input"