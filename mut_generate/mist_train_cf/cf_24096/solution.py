"""
QUESTION:
Determine the type of a credit card based on a given card number. 

Create a function `recognize_credit_card(card_number)` that takes a string of numbers as input, with or without spaces, and returns the type of the credit card (e.g., Visa, Mastercard, Amex). 

The function should recognize the following types of cards based on their prefixes: 
- Visa: 4
- Mastercard: 51, 52, 53, 54, 55
- Amex: 34, 37
"""

def recognize_credit_card(card_number):
    """
    Determine the type of a credit card based on a given card number.

    Args:
        card_number (str): A string of numbers with or without spaces.

    Returns:
        str: The type of the credit card (e.g., Visa, Mastercard, Amex).

    """
    # Remove spaces from the card number
    card_number = card_number.replace(" ", "")

    # Check the prefixes for each card type
    if card_number.startswith(("51", "52", "53", "54", "55")):
        return "Mastercard"
    elif card_number.startswith(("34", "37")):
        return "Amex"
    elif card_number.startswith("4"):
        return "Visa"
    else:
        return "Unknown"