"""
QUESTION:
Write a recursive function `compute_average` that computes the average of a list of numbers without using the sum() function. The function should handle empty lists, NaN values, and duplicate values, and should have a time complexity of O(n), where n is the length of the list. If the list contains any NaN values, the function should return NaN. If the list is empty, the function should return 0. The function should only consider unique values when computing the average.
"""

import math

def compute_average(lst):
    if len(lst) == 0:
        return 0

    total = 0
    count = 0
    has_nan = False
    unique_values = set()

    def recursive_average(lst):
        nonlocal total, count, has_nan, unique_values

        if len(lst) == 0:
            return

        num = lst[0]

        if isinstance(num, float) and math.isnan(num):
            has_nan = True
            return

        if num not in unique_values:
            total += num
            count += 1
            unique_values.add(num)

        recursive_average(lst[1:])

    recursive_average(lst)

    if has_nan:
        return math.nan

    return total / count