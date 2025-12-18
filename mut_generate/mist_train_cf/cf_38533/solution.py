"""
QUESTION:
Implement a function `processPowers(heroPowers, minionPowers)` that takes two lists of integers representing hero powers and minion powers, and returns a list of integers representing the powers after the interactions have been resolved. The interactions are determined by the following rules: if the hero power is greater than the minion power, the hero power is reduced by the value of the minion power; if the minion power is greater than or equal to the hero power, the minion power is reduced by the value of the hero power; if the hero power and minion power are equal, both powers are reduced to 0. The function should return the resulting list of powers after the interactions have been resolved.
"""

from typing import List

def processPowers(heroPowers: List[int], minionPowers: List[int]) -> List[int]:
    result = []
    for hero, minion in zip(heroPowers, minionPowers):
        if hero > minion:
            result.append(hero - minion)
        elif minion >= hero:
            result.append(minion - hero)
    return result