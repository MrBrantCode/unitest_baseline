"""
QUESTION:
Given an array of time points representing Teemo's attacking time series, a poisoning time duration per Teemo's attacking, and assuming Teemo attacks at the very beginning of a specific time point, write a function `findPoisonedDuration` that calculates the total time Ashe is in poisoned condition. The function should take two parameters: `timeSeries` (an array of integers) and `duration` (an integer). The length of `timeSeries` won't exceed 10000 and all numbers are non-negative integers that won't exceed 10,000,000.
"""

def findPoisonedDuration(timeSeries, duration):
    if not timeSeries:
        return 0
    total_poison_time = 0
    for i in range(len(timeSeries) - 1):
        total_poison_time += min(timeSeries[i + 1] - timeSeries[i], duration)
    return total_poison_time + duration