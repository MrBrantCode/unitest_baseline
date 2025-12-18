"""
QUESTION:
Write a function `count_freq` that takes a list of numeric values and returns a tuple containing a dictionary and an integer or string. The dictionary should include the frequency of each distinct element that appears more than once in the list, and the integer or string should be the product of these frequencies. If no element appears more than once, return a dictionary with no elements and a string "No element found with frequency more than 1".
"""

from collections import Counter
import math


def count_freq(lst):
    # Count the occurences of each element in the list
    freq = dict(Counter(lst))
    
    # Remove elements that occur only once
    freq = {k: v for k, v in freq.items() if v > 1}

    # Calculate the product of frequencies
    prod = math.prod(freq.values()) if len(freq.values()) > 0 else "No element found with frequency more than 1"

    return freq, prod