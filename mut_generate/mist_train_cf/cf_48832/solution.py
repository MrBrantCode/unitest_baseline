"""
QUESTION:
Write a function `find_max(arr)` that takes a two-dimensional array of integers as input and returns a list of tuples. Each tuple contains the maximum value in each sub-array and its corresponding index (the index of the first occurrence if multiple highest values exist). Ensure that the input array and sub-arrays are not empty and contain only integers. If these conditions are not met, return an error message.
"""

def find_max(arr):
    # Check if main array is not empty
    if len(arr) == 0:
        return "Error: The main array is empty."

    max_values = []

    for sub_arr in arr:
        # Check if sub-array is not empty
        if len(sub_arr) == 0:
            return "Error: One or more sub-arrays are empty."
        # Check if sub-array contains only integers
        if not all(isinstance(i, int) for i in sub_arr):
            return "Error: The array should contain only integers."

        max_value = max(sub_arr)
        max_index = sub_arr.index(max_value)
        max_values.append((max_value, max_index))

    return max_values