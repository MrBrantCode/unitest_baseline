"""
QUESTION:
Implement the `calculateScore` function to compute the score using the formula: `score = sum((expected_i / a_i) * log10(expected_i / a_i))` for all `i` from 1 to `n`, where `n` is the length of the vectors. The function takes two parameters: `expected` and `a`, both of which are lists of floating-point numbers of the same length. The function should return the calculated score.

Function signature: `def calculateScore(expected: List[float], a: List[float]) -> float:`
"""

from typing import List
import numpy as np

def calculateScore(expected: List[float], a: List[float]) -> float:
    expected_arr = np.array(expected)
    a_arr = np.array(a)
    score = (expected_arr / a_arr * np.log10(expected_arr / a_arr)).sum()
    return score