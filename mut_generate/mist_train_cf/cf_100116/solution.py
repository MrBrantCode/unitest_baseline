"""
QUESTION:
Write a function `max_product(arr)` that finds the maximum product of two numbers in an array containing both positive and negative integers. The function should return `None` if the length of the array is less than 2.
"""

def max_product(arr):
    if len(arr) < 2:
        return None

    max_product = arr[0] * arr[1]

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] * arr[j] > max_product:
                max_product = arr[i] * arr[j]

    return max_product