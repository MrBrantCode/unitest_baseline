"""
QUESTION:
Write a function named `find_second_largest` that takes an array of numbers as input and returns the second largest number without using built-in functions or methods to find the maximum or second maximum value. Assume the input array contains at least two distinct elements. If there is no second largest number (i.e., all elements are the same), return negative infinity.
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