"""
QUESTION:
Given a list of floating point numbers, write a function `weighted_mode(lst)` that calculates the weighted mode where the weight of each number is the number itself, considering up to 3 decimal places. The function should return the number with the highest weight.
"""

from collections import Counter

def weighted_mode(lst):
    freqs = Counter(lst)
    weights = {}
    for num, freq in freqs.items():
        weight = num * freq
        weights[round(num, 3)] = round(weight, 3)
    mode = max(weights, key=weights.get)
    return mode