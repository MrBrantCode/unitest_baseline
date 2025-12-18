"""
QUESTION:
Given a multidimensional array of integers, implement a function `avg_max(arr)` that calculates the average of the maximum values in each sub-array. The function should round the average to 2 decimal places.
"""

def avg_max(arr):
    max_values = [max(sub_arr) for sub_arr in arr]
    return round(sum(max_values) / len(max_values), 2)