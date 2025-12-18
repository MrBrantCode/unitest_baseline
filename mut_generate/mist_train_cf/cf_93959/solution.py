"""
QUESTION:
Create a function `sum_array_elements` that takes an array of integers as input and returns the sum of all unique non-negative numbers in the array.
"""

def sum_array_elements(arr):
    # Create a set to store the unique positive numbers
    unique_numbers = set()

    # Initialize the sum variable
    summation = 0

    # Iterate through the array
    for num in arr:
        # Exclude negative numbers
        if num >= 0:
            # Add the number to the unique_numbers set
            unique_numbers.add(num)

    # Sum all the unique positive numbers
    summation = sum(unique_numbers)

    return summation