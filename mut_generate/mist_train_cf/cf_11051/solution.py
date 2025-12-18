"""
QUESTION:
Write a function named `replace_odd_numbers` that takes an array of integers as input and returns the array with all odd numbers replaced with the sum of their adjacent even numbers. If there are no adjacent even numbers, replace the odd number with 0.
"""

def replace_odd_numbers(arr):
    """
    This function takes an array of integers as input, replaces all odd numbers with 
    the sum of their adjacent even numbers, and returns the updated array. If there 
    are no adjacent even numbers, it replaces the odd number with 0.
    """
    
    # Iterate through the array
    for i in range(len(arr)):
        # Check if the number is odd
        if arr[i] % 2 != 0:
            # Check if there are adjacent even numbers
            if i > 0 and i < len(arr) - 1 and arr[i-1] % 2 == 0 and arr[i+1] % 2 == 0:
                # Replace the odd number with the sum of its adjacent even numbers
                arr[i] = arr[i-1] + arr[i+1]
            else:
                # Replace the odd number with 0
                arr[i] = 0
    
    return arr