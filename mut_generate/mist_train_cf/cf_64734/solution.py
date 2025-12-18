"""
QUESTION:
Write a function named 'second_to_last_min' that takes an array of distinct integers as input and returns a tuple containing the second-to-last minimum value and its index in the array. The array can be of variable length.
"""

def second_to_last_min(arr):
    # Initialize the lowest and second lowest values
    low1, low2 = float('inf'), float('inf')

    # Initialize the index of the lowest and second lowest values
    idx1, idx2 = -1, -1

    # Go through the elements of the array
    for i in range(len(arr)):
        # Update the lowest and second lowest values and their indices
        if arr[i] < low1:
            low2 = low1
            idx2 = idx1
            low1 = arr[i]
            idx1 = i
        elif arr[i] < low2:
            low2 = arr[i]
            idx2 = i

    # Return the second lowest value and its index
    return low2, idx2