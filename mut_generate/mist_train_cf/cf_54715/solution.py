"""
QUESTION:
Write a function named `custom_stddev` that takes a list of numbers as input and returns the standard deviation of the numbers, disregarding any number that repeats more than twice in the list. If the resulting list has one or zero elements, return 0.
"""

import statistics
from collections import Counter

def custom_stddev(data):
    counter = Counter(data)     
    new_data = [x for x in data if counter[x] <= 2]
    return statistics.stdev(new_data) if len(new_data) > 1 else 0