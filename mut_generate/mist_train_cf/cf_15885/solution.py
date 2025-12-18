"""
QUESTION:
Create a function named `sum_array_elements` that takes an array of integers as input, sums all unique non-negative integers, and returns the result. The function should exclude any negative numbers from the summation and count duplicate numbers only once.
"""

def sum_array_elements(arr):
    # Create a set to store the unique positive numbers
    unique_numbers = set()

    # Iterate through the array
    for num in arr:
        # Exclude negative numbers
        if num >= 0:
            # Add the number to the unique_numbers set
            unique_numbers.add(num)

    # Sum all the unique positive numbers
    return sum(unique_numbers)