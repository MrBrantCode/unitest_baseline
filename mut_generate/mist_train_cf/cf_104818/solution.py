"""
QUESTION:
Write a function named `find_max_min` that takes an array of integers as a parameter and returns a tuple containing the maximum and minimum values in the array using only a single loop. Do not use any built-in functions or libraries to find the maximum and minimum values.
"""

def find_max_min(arr):
    # Initialize max_value and min_value with the first element of the array
    max_value = arr[0]
    min_value = arr[0]
    
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Update max_value if current element is greater
        if arr[i] > max_value:
            max_value = arr[i]
        # Update min_value if current element is smaller
        if arr[i] < min_value:
            min_value = arr[i]
    
    # Return the maximum and minimum values as a tuple
    return (max_value, min_value)