"""
QUESTION:
Implement a function `fitter(sig1d)` that takes a 1-dimensional signal `sig1d` as input and returns the index of the first element greater than the average of all elements in the signal. If no such element exists, return -1. The input signal `sig1d` contains at least one element.
"""

from typing import List

def fitter(sig1d: List[float]) -> int:
    average = sum(sig1d) / len(sig1d)
    for i, val in enumerate(sig1d):
        if val > average:
            return i
    return -1