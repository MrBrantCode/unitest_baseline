"""
QUESTION:
Write a function named `calculate_sum` that takes two parameters: an array of integers `arr` and an integer `limit`. The function should calculate the sum of elements in `arr` that are divisible by 3 without exceeding the given `limit`. If no elements in `arr` are divisible by 3, the function should return -1. If the sum exceeds the `limit`, the function should return the sum of elements that are divisible by 3 before the limit is exceeded.
"""

def calculate_sum(arr, limit):
    sum = 0
    divisible_by_3 = False

    for i in range(len(arr)):
        if arr[i] % 3 == 0:
            sum += arr[i]
            divisible_by_3 = True

            if sum > limit:
                sum -= arr[i]
                break

    if divisible_by_3:
        return sum
    else:
        return -1