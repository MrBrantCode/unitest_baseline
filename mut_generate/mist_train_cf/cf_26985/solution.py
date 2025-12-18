"""
QUESTION:
Implement a function `make_choice` that takes in a 2D NumPy array `history` representing the previous moves of both players and an integer `currentCount` representing the current round number. The function should return the player's choice for the current round (0 for defect, 1 for cooperate) and a tuple containing the updated current count, a boolean indicating whether the player defected, and a boolean indicating whether the player has defected previously, based on the following strategy: 
- If the opponent defected in the previous round and the current count is greater than or equal to 1, the player should defect.
- If the opponent cooperated in the previous round and the current count is greater than or equal to 1, and the player has not defected previously, the player should cooperate.
- If none of the above conditions are met, the player should cooperate.
"""

import numpy as np

def make_choice(history, currentCount):
    if history.shape[1] >= 1 and history[1, -1] == 0:
        return 0, (currentCount, True, True)
    else:
        hasDefected = False
        if currentCount >= 1 and not hasDefected:
            return 1, (currentCount, False, False)
        else:
            return 1, (currentCount, False, False)