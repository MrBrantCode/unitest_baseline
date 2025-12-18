"""
QUESTION:
Create a function `sum_of_integers` that takes an array of integers as an argument. The function should return the sum of all unique, positive integers in the array, ignoring any negative integers and duplicates. The function must also validate the input, raising an exception if the input is not an array or if the array contains non-integer values or nested arrays.
"""

def sum_of_integers(arr):
    # Check if the input argument is a valid array of integers
    if not isinstance(arr, list):
        raise Exception("Invalid input, argument must be an array.")
    for num in arr:
        if not isinstance(num, int) or isinstance(num, list):
            raise Exception("Invalid input, array contains non-integer values or nested arrays.")

    # Remove duplicates from the array
    arr = list(set(arr))

    # Calculate the sum of positive integers in the array
    return sum([num for num in arr if num > 0])