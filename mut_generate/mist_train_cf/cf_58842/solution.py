"""
QUESTION:
Write a function `sum_and_location` that takes a two-dimensional array of integers as input, where each sub-array may have different lengths. The function should return the sum of all elements in the array and the row and column of the maximum value. If there are multiple occurrences of the maximum value, the function should return the row and column of its first instance.
"""

def sum_and_location(arr):
    total = 0
    max_val = arr[0][0]
    max_pos = (0, 0)
    for i, sub_arr in enumerate(arr):
        for j, num in enumerate(sub_arr):
            total += num
            if num > max_val:
                max_val = num
                max_pos = (i, j)
    return total, max_pos[0], max_pos[1]