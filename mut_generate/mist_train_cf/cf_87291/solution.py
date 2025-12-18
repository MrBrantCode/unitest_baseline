"""
QUESTION:
Create a function named `sum_of_integers` that takes one argument as an array of integers, ignores negative integers and duplicates, and returns the sum of the remaining integers. The function should raise a custom exception if the input argument is not a valid array of integers, contains non-integer values, or contains nested arrays.
"""

def sum_of_integers(arr):
    if not isinstance(arr, list):
        raise Exception("Invalid input, argument must be an array.")
    for num in arr:
        if not isinstance(num, int):
            raise Exception("Invalid input, array contains non-integer values.")
        if isinstance(num, list):
            raise Exception("Invalid input, array contains nested arrays.")

    arr = list(set(arr))
    total = sum([num for num in arr if num > 0])
    return total