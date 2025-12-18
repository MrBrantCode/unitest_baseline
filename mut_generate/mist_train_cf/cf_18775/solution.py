"""
QUESTION:
Write a function named `multiply_and_sort` that takes an array of positive integers as input, multiplies each even number in the array by 3, and returns the resulting numbers in a new array sorted in descending order.
"""

def multiply_and_sort(arr):
    result = []
    for num in arr:
        if num % 2 == 0:
            result.append(num * 3)
    result = sorted(result, reverse=True)
    return result