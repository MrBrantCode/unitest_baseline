"""
QUESTION:
Implement a `CardDrawnProbability` class with an `__init__` method and a `calculate_probability` method. The `__init__` method should take in six parameters: `total_cards`, `specific_cards`, `num_drawn`, `num_specific_drawn`, `turn`, and `num_specific_required`. The `calculate_probability` method should calculate the probability of drawing a specific card on a given turn, considering the number of cards drawn and the number of specific cards in the deck.
"""

import math

def card_drawn_probability(total_cards, specific_cards, num_drawn, num_specific_drawn, turn, num_specific_required):
    remaining_cards = total_cards - num_drawn
    remaining_specific_cards = specific_cards - num_specific_drawn

    if turn == 1:
        probability = remaining_specific_cards / remaining_cards
    else:
        remaining_cards -= (turn - 1) * num_drawn
        remaining_specific_cards -= (turn - 1) * num_specific_drawn
        probability = 1 - (math.comb(remaining_cards - remaining_specific_cards, num_specific_required) / math.comb(remaining_cards, num_specific_required))

    return probability