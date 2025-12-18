"""
QUESTION:
Develop a function named `cumulative_sum` that calculates the cumulative sum of all numerical values in a nested tuple structure. The function should be able to navigate through nested tuples and disregard any non-numeric entities. The input dataset should only consist of numbers and tuples.
"""

def cumulative_sum(tuples):
    total = 0
    for item in tuples:
        if isinstance(item, tuple):    # if item is a tuple, navigate
            total += cumulative_sum(item)
        elif isinstance(item, (int, float)):   # if item is a numerical value
            total += item
    return total