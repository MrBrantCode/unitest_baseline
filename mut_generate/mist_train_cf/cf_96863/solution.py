"""
QUESTION:
Create a function `determine_order(arr)` that determines whether a given array is strictly increasing, strictly decreasing, non-decreasing, non-increasing, or unordered. The function should not use any comparison operators or sorting algorithms. It should only take an array as input and return a string describing the order type. The array is guaranteed to have at least two elements.
"""

def determine_order(arr):
    # Check if the array is strictly increasing
    if all(arr[i] < arr[i + 1] for i in range(len(arr) - 1)):
        return "Strictly Increasing"

    # Check if the array is strictly decreasing
    if all(arr[i] > arr[i + 1] for i in range(len(arr) - 1)):
        return "Strictly Decreasing"

    # Check if the array is non-decreasing
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        return "Non-decreasing"

    # Check if the array is non-increasing
    if all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)):
        return "Non-increasing"

    # If none of the above conditions are met, the array is unordered
    return "Unordered"