"""
QUESTION:
Compute a function `compute_opponent_impact` that takes four parameters: `our_size`, `opponent_size`, `our_position`, and `opponent_position`. The function should calculate the impact score of an opponent in a game scenario. The impact score is determined by the Manhattan distance between the player's and opponent's positions multiplied by the difference in their sizes. The function should return the calculated impact score. The function parameters are as follows:
- `our_size`: The size of the player, represented as an integer.
- `opponent_size`: The size of the opponent, represented as an integer.
- `our_position`: The position of the player, represented as a tuple of two integers.
- `opponent_position`: The position of the opponent, represented as a tuple of two integers.
The return value should be an integer representing the impact score.
"""

from typing import Tuple

def compute_opponent_impact(our_size: int, opponent_size: int, our_position: Tuple[int, int], opponent_position: Tuple[int, int]) -> int:
    distance = abs(our_position[0] - opponent_position[0]) + abs(our_position[1] - opponent_position[1])
    size_difference = our_size - opponent_size
    impact_score = distance * size_difference
    return impact_score