"""
QUESTION:
Implement the `generate_dice_pairings` function that takes a list of unique dice names and an integer representing the number of pairs to be formed. The function should return a list of all possible pairings of the dice names, where each pair consists of two distinct dice names and the pairings are repeated for the specified number of pairs.
"""

from itertools import permutations

def generate_dice_pairings(dice_names, num_pairs):
    dice_pairs = list(permutations(dice_names, 2))
    pairings = []
    for _ in range(num_pairs):
        pairings.extend(dice_pairs)
    return pairings