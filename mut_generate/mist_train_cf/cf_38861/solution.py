"""
QUESTION:
Implement a function `hand_value` that calculates the value of a player's hand in a card game. The function should take a list of cards as input where each card is represented as an integer (2-10 for numbered cards, 11-13 for Jack, Queen, King, and 14 for Ace). The function should return the total value of the hand, considering that Aces can have a value of 1 or 11, whichever yields a better hand value without exceeding 21.
"""

def calculate_hand_value(cards):
    """Calculate player's hand value and return it"""
    card_sum = 0
    aces = 0

    for card in cards:
        if card == 14:
            aces += 1
        elif 11 <= card <= 13:
            card_sum += 10
        else:
            card_sum += card

    if aces > 0:
        for _ in range(aces):
            if card_sum + 11 <= 21:
                card_sum += 11
            else:
                card_sum += 1

    return card_sum