"""
QUESTION:
Write a function called `calculate_mode` that takes a list of numbers as input and returns a list of the mode(s), where the mode is the number that appears most frequently in the list. If there are multiple modes (i.e., multiple numbers appear with the same highest frequency), the function should return all of them.
"""

import collections

def calculate_mode(array):
    data = collections.Counter(array)
    return [k for k, v in dict(data).items() if v == max(list(data.values()))]