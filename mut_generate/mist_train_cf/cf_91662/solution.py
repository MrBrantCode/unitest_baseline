"""
QUESTION:
Replace all odd numbers in an array with the sum of their adjacent even numbers. If an odd number has no adjacent even numbers, replace it with 0. Write a function named `replace_odd_numbers` that takes an array of integers as input and returns the modified array.
"""

def replace_odd_numbers(arr):
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            if i > 0 and i < len(arr) - 1 and arr[i-1] % 2 == 0 and arr[i+1] % 2 == 0:
                arr[i] = arr[i-1] + arr[i+1]
            else:
                arr[i] = 0
    return arr