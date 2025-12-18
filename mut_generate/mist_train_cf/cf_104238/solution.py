"""
QUESTION:
Write a function named `sum_greater_than_10_divisible_by_3` that takes a 2D array of integers as input and returns the sum of all elements that are greater than 10 and divisible by 3, ignoring any negative numbers. The input array will have at most 100 rows, each with at most 100 columns, and will contain integers between -1000 and 1000 inclusive.
"""

def sum_greater_than_10_divisible_by_3(arr):
    # Initialize the sum
    total_sum = 0
    
    # Iterate through each row in the array
    for row in arr:
        # Iterate through each element in the row
        for num in row:
            # Check if the element is positive, greater than 10, and divisible by 3
            if num > 10 and num % 3 == 0:
                total_sum += num
    
    # Return the final sum
    return total_sum