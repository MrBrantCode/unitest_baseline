"""
QUESTION:
Design a function named `find_largest_number` that takes an array of integers as input and returns the largest number in the array without using any built-in sorting or max functions. The function should have a time complexity of O(n), where n is the length of the array.
"""

def find_largest_number(arr):
    # Initialize the largest number to the first element in the array
    largest_number = arr[0]
    
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # If the current element is larger than the largest number, update the largest number
        if arr[i] > largest_number:
            largest_number = arr[i]
    
    return largest_number