"""
QUESTION:
Write a function `min_2d_array` that takes a 2D array of numbers as input and returns the minimum value in the array along with its position(s) as a list of tuples. The function should work with 2D arrays of any size and should handle cases where the minimum value appears multiple times.
"""

def min_2d_array(arr):
    # Initialize minimum value to be a large number
    min_val = float('inf')
    positions = []

    # Loop through the 2D array to find the minimum value
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] < min_val:
                min_val = arr[i][j]
                # Store the positions of the new minimum value
                positions = [(i, j)]
            elif arr[i][j] == min_val:
                # If current value is equal to minimum value, add its position to the list
                positions.append((i, j))

    return min_val, positions