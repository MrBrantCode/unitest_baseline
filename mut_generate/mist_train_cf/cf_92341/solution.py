"""
QUESTION:
Write a function named `sum_positive_even` that takes an array of integers as input and returns the sum of all positive even numbers in the array. If the array does not contain any positive even numbers, the function should return 0.
"""

def sum_positive_even(arr):
    # Initialize the sum to 0
    sum = 0

    # Iterate through each element in the array
    for num in arr:
        # Check if the number is positive and even
        if num > 0 and num % 2 == 0:
            # Add the number to the sum
            sum += num

    # Return the sum
    return sum