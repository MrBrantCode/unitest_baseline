"""
QUESTION:
Create a function named `average_sum` that takes a 2D array of numbers as input. The function should calculate the sum of numbers across all sub-arrays and return their average. If a sub-array is empty, it should be ignored in the calculation. The function should handle cases where all sub-arrays are empty and return 0 in such cases.
"""

def average_sum(arr):
    sum_of_sums = 0
    count = 0

    for sub_arr in arr:
        if len(sub_arr) > 0:
            sum_of_sums += sum(sub_arr)
            count += 1

    if count == 0:
        return 0

    return sum_of_sums / count