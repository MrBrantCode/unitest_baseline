"""
QUESTION:
Write a function named `find_second_largest` that takes an array of integers as input and returns the second largest number in the array without using any built-in functions or methods to find the maximum or second maximum value. The array can contain duplicate numbers, and if there is no second largest number (i.e., all numbers are the same), the function should return a value to indicate that (in this case, negative infinity).
"""

def find_second_largest(arr):
    # Initialize the maximum and second maximum variables
    max_num = arr[0]
    second_max = float('-inf')

    # Traverse through the array
    for i in range(1, len(arr)):
        # If the current element is greater than the maximum, update both maximum and second maximum
        if arr[i] > max_num:
            second_max = max_num
            max_num = arr[i]
        # If the current element is between the maximum and second maximum, update only the second maximum
        elif arr[i] > second_max and arr[i] != max_num:
            second_max = arr[i]

    # Return the second maximum number
    return second_max