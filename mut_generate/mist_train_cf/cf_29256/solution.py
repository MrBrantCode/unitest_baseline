"""
QUESTION:
You are given a list of energy values representing changes in energy levels at different time intervals. The device starts with an initial energy level of 0 and cannot operate if its energy level drops below 0. Write a function `minInitialEnergy` that takes in a list of energy values and returns the minimum initial energy level required for the device to operate continuously throughout the time intervals.
"""

from typing import List

def minInitialEnergy(energyValues: List[int]) -> int:
    minInitial = 0
    currentEnergy = 0

    for energy in energyValues:
        currentEnergy += energy
        if currentEnergy < 0:
            minInitial += abs(currentEnergy)
            currentEnergy = 0

    return minInitial