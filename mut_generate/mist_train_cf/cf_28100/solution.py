"""
QUESTION:
Complete the function `calculate_reward(closestPoints)` where `closestPoints` is a list of points in a 2D space represented as tuples (x, y). The reward is calculated based on the number of closest points: if the number of closest points is greater than 0, the reward is the square of the number of closest points multiplied by 100, otherwise the reward is -1000. Function signature: `def calculate_reward(closestPoints: List[Tuple[int, int]]) -> int`
"""

from typing import List, Tuple

def entance(closestPoints: List[Tuple[int, int]]) -> int:
    reward = -1000
    numPt = len(closestPoints)
    if numPt > 0:
        reward += numPt ** 2 * 100
    return reward