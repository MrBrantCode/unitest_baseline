"""
QUESTION:
Write a function named `sum_positive_elements` that takes an array of numbers as input and returns the sum of all non-negative numbers in the array. The function should exclude any negative numbers from the summation.
"""

def sum_positive_elements(arr):
    # Initialize a variable to hold the sum
    total = 0
    
    # Iterate through the array
    for num in arr:
        # Check if the number is positive
        if num >= 0:
            # Add the positive number to the sum
            total += num
    
    # Return the sum of positive elements
    return total