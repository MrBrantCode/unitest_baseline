"""
QUESTION:
Write a function `determine_order(arr)` that takes an array of integers as input and returns a string indicating whether the array is "Strictly Increasing", "Strictly Decreasing", "Non-decreasing", "Non-increasing", or "Unordered". The function should not use any comparison operators or sorting algorithms. The array will contain at least two elements.
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