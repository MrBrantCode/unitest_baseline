"""
QUESTION:
Create a function `min_swaps_to_descending(arr)` that takes an array of integers with at least one repeated number as input and returns the minimum number of swaps needed to sort the array in descending order.
"""

def min_swaps_to_descending(arr):
    n = len(arr)
    sorted_arr = sorted(arr, reverse=True)
    index_map = {val: i for i, val in enumerate(arr)}
    swaps = 0
    for i in range(n):
        curr_val = arr[i]
        expected_val = sorted_arr[i]
        if curr_val != expected_val:
            expected_index = index_map[expected_val]
            arr[i], arr[expected_index] = arr[expected_index], arr[i]
            index_map[curr_val] = expected_index
            index_map[expected_val] = i
            swaps += 1
    return swaps