"""
QUESTION:
Write a function named `minStamps` that takes a list of distinct postage stamp denominations (`stamps`) and a target cumulative value (`target`) as input, and returns the minimum number of stamps required to achieve the target cumulative value. The function should return infinity if it's impossible to reach the target value with the given stamp denominations.
"""

def minStamps(stamps, target):
    minNumStamps = [float('inf')] * (target + 1)
    minNumStamps[0] = 0
    for stamp in stamps:
        for value in range(stamp, target + 1):
            minNumStamps[value] = min(minNumStamps[value], minNumStamps[value - stamp] + 1)
    return float('inf') if minNumStamps[target] == float('inf') else minNumStamps[target]