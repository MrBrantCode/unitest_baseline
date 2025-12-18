"""
QUESTION:
Write a function named find_max_min() that takes an array of integers as input and returns the maximum and minimum values in the array. The function must not use built-in functions or methods such as max() or min(). The function must find the maximum and minimum values in a single traversal of the array. The array may contain duplicate values.
"""

def find_max_min(arr):
    """
    Find the maximum and minimum values in an array without using built-in functions.

    Args:
        arr (list): A list of integers.

    Returns:
        tuple: A tuple containing the maximum and minimum values.
    """
    # Initialize the maximum and minimum values to the first element of the array
    max_value = arr[0]
    min_value = arr[0]

    # Iterate through the array
    for num in arr:
        # Update the maximum value if the current number is greater
        if num > max_value:
            max_value = num
        # Update the minimum value if the current number is smaller
        if num < min_value:
            min_value = num

    # Return the maximum and minimum values
    return max_value, min_value