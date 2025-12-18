"""
QUESTION:
Write a function `calculate_sum` that calculates the sum of the elements of an array with float values, excluding any negative values and rounding the final sum to two decimal places. The function should take one argument, an array of float values, and return the rounded sum.
"""

def calculate_sum(arr):
    # Initialize sum variable
    total_sum = 0
    
    # Iterate through each element in the array
    for num in arr:
        # Exclude negative values
        if num >= 0:
            # Add the positive value to the sum
            total_sum += num
    
    # Round the sum to two decimal places
    total_sum = round(total_sum, 2)
    
    # Return the rounded sum
    return total_sum