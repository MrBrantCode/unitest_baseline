"""
QUESTION:
Write a function named sum_positive that takes an array of integers as input. The function should return the sum of all positive integers in the array. If the array is empty or does not contain any positive integers, the function should return 0. The solution should have a time complexity of O(n), where n is the length of the array.
"""

def sum_positive(arr):
    # Initialize sum to 0
    sum = 0
    
    # Iterate through each element in the array
    for num in arr:
        # Check if the element is positive
        if num > 0:
            # Add the positive element to the sum
            sum += num
    
    # Return the final sum
    return sum