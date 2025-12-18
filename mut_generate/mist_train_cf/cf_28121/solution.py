"""
QUESTION:
Implement a function `calculate_entropy` that calculates the entropy of an image's histogram. The function takes a list of integers representing the histogram of the image as input, where the value at index `i` represents the frequency of intensity level `i`. The function should return the calculated entropy value as a float. The entropy is calculated using the formula `H = - ∑(p_i * log2(p_i))`, where `p_i` represents the probability of occurrence of the `i`th intensity level in the image.
"""

from typing import List
import math

def calculate_entropy(histogram: List[int]) -> float:
    total_pixels = sum(histogram)
    probabilities = [count / total_pixels for count in histogram if count != 0]
    entropy = -sum(p * math.log2(p) for p in probabilities)
    return entropy