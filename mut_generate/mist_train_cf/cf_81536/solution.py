"""
QUESTION:
Given a list of unique integers representing the order in which light bulbs are turned on, write a function `numTimesAllBlue` that returns the number of moments when all the turned-on bulbs are blue, meaning they form a consecutive sequence with no off bulbs in between. The input list `light` is a permutation of numbers from 1 to `n`, where `n` is the length of the list. The function should run in efficient time and space complexity.
"""

def numTimesAllBlue(light):
    right_most_on_bulb = max_bulb = moments = 0
    for i, bulb in enumerate(light, 1): 
        max_bulb = max(max_bulb, bulb)
        right_most_on_bulb += 1
        if right_most_on_bulb == max_bulb: 
            moments += 1
    return moments