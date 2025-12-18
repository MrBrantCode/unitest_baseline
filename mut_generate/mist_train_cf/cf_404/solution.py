"""
QUESTION:
Write a function `average_positive_numbers` that calculates the average of all positive integers in a given array. The function should ignore non-integer values, zeros, and negative numbers. It should also handle empty arrays by returning 0, and its time complexity should not exceed O(n), where n is the length of the array.
"""

def average_positive_numbers(arr):
    count = 0
    total = 0

    for num in arr:
        if isinstance(num, int) and num > 0:
            total += num
            count += 1

    return total / count if count > 0 else 0