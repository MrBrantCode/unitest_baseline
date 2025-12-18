"""
QUESTION:
Develop a Python function called `unique_elements` that takes an array of mixed floating-point and Boolean values as input and returns the five unique elements with the least occurrence. If there are less than five unique elements, return all of them. The function should handle arrays of any size and ordering, prioritize elements with the lowest frequency, and consider the order of elements in case of a tie in frequency.
"""

from collections import Counter
from heapq import nsmallest

def unique_elements(arr):
    freq = Counter(arr)
    return nsmallest(min(5, len(freq)), freq, key=freq.get)