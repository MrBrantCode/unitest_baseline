"""
QUESTION:
Write a function `find_largest_number` that takes an array of numbers as input and returns the largest number in the array without using any built-in functions or methods to find the maximum value. Assume the input array is not empty.
"""

def find_largest_number(arr):
    largest = arr[0]  # assume the first element is the largest

    for num in arr:
        if num > largest:
            largest = num

    return largest