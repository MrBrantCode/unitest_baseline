"""
QUESTION:
Write a function `calculate_stats` that takes a list of integers as input and returns the maximum, minimum, and average values. The list contains positive integers ranging from 1 to 1000 and has a length between 10 and 1000.
"""

def calculate_stats(arr):
    """
    This function calculates the maximum, minimum, and average values in a given list of integers.

    Args:
    arr (list): A list of integers.

    Returns:
    tuple: A tuple containing the maximum, minimum, and average values.
    """

    # Initialize variables for maximum, minimum, and sum of elements
    maximum = arr[0]
    minimum = arr[0]
    sum_of_elements = arr[0]

    # Loop through the array starting from the second element
    for i in range(1, len(arr)):
        # Check if current element is greater than current maximum
        if arr[i] > maximum:
            maximum = arr[i]
        # Check if current element is smaller than current minimum
        if arr[i] < minimum:
            minimum = arr[i]
        
        # Add current element to the sum
        sum_of_elements += arr[i]

    # Calculate the average
    average = sum_of_elements / len(arr)

    return maximum, minimum, average