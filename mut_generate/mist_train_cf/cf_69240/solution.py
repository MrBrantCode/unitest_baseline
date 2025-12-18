"""
QUESTION:
Write a function called `solve` that takes an array of integers as input and returns the number of distinct elements and the number of elements that occur exactly once. The function should output these two values. The input array can contain duplicate integers.
"""

from collections import Counter

def solve(arr):
    freq = Counter(arr)
    distinct_elements = len(freq)
    single_occurrence = sum(1 for i in freq.values() if i == 1)
    return distinct_elements, single_occurrence