"""
QUESTION:
Write a function `validate_credit_card_number(card_number)` that takes a string `card_number` as input, validates its type (Visa, MasterCard, American Express, Discover) based on its prefix, and checks its length. The function should return the card type if valid or False otherwise. The prefixes for each card type are:
- Visa: starts with 4 and has a length of 16
- MasterCard: starts with 51, 52, 53, 54, or 55 and has a length of 16
- American Express: starts with 34 or 37 and has a length of 15
- Discover: starts with 6011 and has a length of 16
Assume the input may contain spaces and non-digit characters. The function should not use any external libraries or modules.
"""

def entance(card_number):
    card_number = card_number.replace(" ", "")
    if not card_number.isdigit() or len(card_number) < 13 or len(card_number) > 16:
        return False

    if card_number[0] == '4' and len(card_number) == 16:
        return "Visa"

    if card_number[:2] in ['51', '52', '53', '54', '55'] and len(card_number) == 16:
        return "MasterCard"

    if card_number[:2] in ['34', '37'] and len(card_number) == 15:
        return "American Express"

    if card_number[:4] == '6011' and len(card_number) == 16:
        return "Discover"

    return False