"""
QUESTION:
Write a function named `recursive_sum` that calculates the cumulative sum of all numeric values within a given tuple list, including nested tuples, while ignoring non-numeric values.
"""

def recursive_sum(tuples, cum_sum = 0):
    for i in tuples:
        if isinstance(i, tuple):
            cum_sum = recursive_sum(i, cum_sum)
        elif isinstance(i, (int, float)):
            cum_sum += i
    return cum_sum