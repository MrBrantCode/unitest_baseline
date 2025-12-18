"""
QUESTION:
Create a function `find_min(arr)` that takes an array of positive integers as input and returns the minimum value and its index in the array. The function should not use any built-in functions or libraries.
"""

def find_min(arr):
    # Initialize variables to store the minimum value and its index
    min_val = arr[0]
    min_index = 0
    
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Check if the current element is smaller than the current minimum value
        if arr[i] < min_val:
            # Update the minimum value and its index
            min_val = arr[i]
            min_index = i
    
    # Return the minimum value and its index
    return min_val, min_index