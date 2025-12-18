"""
QUESTION:
Write a function called `second_greatest` that takes an array of integers as input and returns the second greatest value in the array without using any built-in sorting functions or methods. The input array will always contain at least 2 unique integers.
"""

def second_greatest(numbers):
    # Initialize variables to store the maximum and second maximum values
    max_value = float('-inf')
    second_max_value = float('-inf')

    # Iterate over each element in the array
    for num in numbers:
        # Update the maximum and second maximum values accordingly
        if num > max_value:
            second_max_value = max_value
            max_value = num
        elif num > second_max_value:
            second_max_value = num

    return second_max_value