"""
QUESTION:
Develop a function `cum_sum` that calculates the cumulative sum of all numerical elements within a multi-dimensional array, handling non-numeric exceptions by ignoring them. The input array can contain integers, floats, and nested lists of arbitrary depth. The function should return the total sum of all numeric elements in the array.
"""

def cum_sum(arr):
    total_sum = 0
    for i in arr:
        if isinstance(i, list):
            total_sum += cum_sum(i)
        else:
            try:
                total_sum += i
            except TypeError:
                continue
    return total_sum