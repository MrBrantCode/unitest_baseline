"""
QUESTION:
Write a function `find_max_second_max` that takes an array of integers as input and returns a tuple of two tuples, where the first tuple contains the maximum element and its index, and the second tuple contains the second maximum element and its index. If the array has less than two elements, the function should return `None` for the second maximum element and its index.
"""

def find_max_second_max(arr):
    if len(arr) == 1:
        return (arr[0], 0), None
    
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            return (arr[0], 0), (arr[1], 1)
        else:
            return (arr[1], 1), (arr[0], 0)

    else:
        if arr[0] > arr[1]:
            max_val, max_idx = arr[0], 0
            second_max_val, second_max_idx = arr[1], 1
        else:
            max_val, max_idx = arr[1], 1
            second_max_val, second_max_idx = arr[0], 0

        for i in range(2, len(arr)):
            if arr[i] > max_val:
                second_max_val, second_max_idx = max_val, max_idx
                max_val, max_idx = arr[i], i
            elif arr[i] > second_max_val:
                second_max_val, second_max_idx = arr[i], i

        return (max_val, max_idx), (second_max_val, second_max_idx)