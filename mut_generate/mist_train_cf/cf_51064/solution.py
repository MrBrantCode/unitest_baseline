"""
QUESTION:
Create a function named `find_max` that accepts an array of integers as input and returns the maximum value present in the array without using the built-in `max` function.
"""

def find_max(arr):
    max_val = arr[0]  # initialize max value with the first element
    for num in arr:
        if num > max_val:
            max_val = num  # update max value if current number is greater than max_val
    return max_val