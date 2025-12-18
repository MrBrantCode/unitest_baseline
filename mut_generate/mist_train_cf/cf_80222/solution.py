"""
QUESTION:
Create a function `identify_card(card_number)` that classifies a given credit card number into one of the four major types: AMEX, VISA, Discover, or MasterCard, based on the card's starting digits and length. The function should return "Unknown" if the card number does not match any of these patterns.

The classification rules are as follows:
- VISA: Starts with 4, Length 13 or 16
- MasterCard: Starts with 51-55 or 2221-2720, Length 16
- AMEX: Starts with 34 or 37, Length 15
- Discover: Starts with 6011, 622126-622925, 644-649, 65, Length 16
"""

def identify_card(card_number):
    card = card_number.replace(" ", "")
    card_len = len(card)

    if card_len == 15 and (card.startswith("34") or card.startswith("37")): return "AMEX"
    elif 13 <= card_len <= 16 and card.startswith("4"): return "VISA"
    elif card_len == 16 and (card.startswith("6011") or card.startswith("65") or int(card[0:6]) in range(622126, 622925 + 1) or int(card[0:3]) in range(644, 649 + 1)):
        return "Discover"
    elif card_len == 16 and ((int(card[0:2]) in range(51, 55 + 1)) or (int(card[0:4]) in range(2221, 2720 + 1))): return "MasterCard"

    return "Unknown"