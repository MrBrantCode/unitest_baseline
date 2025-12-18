"""
QUESTION:
Write a function named `calculate_average` that takes an array of integers as input and returns the average of the array. The function should handle arrays containing negative integers, empty arrays (returning 0 as the average), and arrays with up to 10^6 elements.
"""

def calculate_average(arr):
    if len(arr) == 0:  # Handle empty array
        return 0

    total = 0
    for num in arr:
        total += num

    average = total / len(arr)
    return average