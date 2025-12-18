"""
QUESTION:
Implement a function called `selection_sort` that takes a list of integers as input, sorts it in ascending order in O(n^2) time complexity, removes any duplicate elements, and returns the resulting sorted list. The function should use a recursive approach.
"""

def selection_sort(arr):
    if len(arr) <= 1:
        return arr

    min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i

    if min_idx != 0:
        arr[0], arr[min_idx] = arr[min_idx], arr[0]

    sorted_arr = [arr[0]]
    remaining_arr = arr[1:]

    if len(remaining_arr) > 0 and remaining_arr[0] != sorted_arr[0]:
        sorted_arr.extend(selection_sort(remaining_arr))
    elif len(remaining_arr) > 0:
        sorted_arr.extend(selection_sort(remaining_arr[1:]))
    return sorted_arr