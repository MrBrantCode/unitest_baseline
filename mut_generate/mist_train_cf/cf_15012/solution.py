"""
QUESTION:
Create a function called `max_difference` that takes an array of numbers (which can include negative numbers and float values) as input and returns the maximum difference between any two numbers in the array. The array must contain at least two elements to find the difference.
"""

def max_difference(arr):
    if len(arr) < 2:
        return None  # There must be at least two elements in the array to find the difference

    max_diff = arr[1] - arr[0]  # Initialize the maximum difference as the difference between the first two elements
    min_element = min(arr[0], arr[1])  # Initialize the minimum element as the smaller of the first two elements

    for i in range(2, len(arr)):
        if arr[i] - min_element > max_diff:
            max_diff = arr[i] - min_element  # Update the maximum difference if a larger one is found
        if arr[i] < min_element:
            min_element = arr[i]  # Update the minimum element if a smaller one is found

    return max_diff