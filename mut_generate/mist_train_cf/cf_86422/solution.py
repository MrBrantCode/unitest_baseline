"""
QUESTION:
Write a function called `average_positive_numbers` that takes an array of integers as input. The function should calculate and return the average of all positive integers in the array, excluding non-integer values, zero, and negative numbers. If the input array is empty or contains no positive integers, the function should return 0. The function's time complexity should not exceed O(n), where n is the length of the input array.
"""

def average_positive_numbers(arr):
    total = sum(num for num in arr if isinstance(num, int) and num > 0)
    count = sum(1 for num in arr if isinstance(num, int) and num > 0)

    return total / count if count > 0 else 0