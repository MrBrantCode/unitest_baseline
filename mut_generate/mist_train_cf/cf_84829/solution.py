"""
QUESTION:
Write a function `most_recurring_value` that takes a list of integers as input and returns the most recurring value and its frequency. The function should handle any list of integers, not just the provided example.
"""

from collections import Counter

def most_recurring_value(arr):
    counter = Counter(arr)
    most_common_element = counter.most_common(1)[0]
    return most_common_element[0], most_common_element[1]