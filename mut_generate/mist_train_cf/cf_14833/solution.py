"""
QUESTION:
Write a function named `calculate_sum_within_limit` that takes an array of numbers and a limit as input and returns the sum of elements in the array without exceeding the given limit.
"""

def calculate_sum_within_limit(arr, limit):
    total_sum = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if total_sum + arr[j] <= limit:
                total_sum += arr[j]
            else:
                break
    return total_sum