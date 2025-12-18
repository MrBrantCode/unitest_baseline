"""
QUESTION:
Write a function named `find_mode` that takes a list of integers as input and returns the mode of the list, which is the integer that appears most frequently in the list. The function should return one of the modes if there are multiple modes.
"""

from collections import Counter

def find_mode(numbers):
    frequency = Counter(numbers)
    return frequency.most_common(1)[0][0]