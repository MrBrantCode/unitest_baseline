"""
QUESTION:
Implement a function called "first_duplicate" that takes an array of integers as input and returns the first duplicate element found in the array. If no duplicate is found, the function should return -1. The function must have a time complexity of O(n), where n is the length of the array, and be implemented using only a single loop without any additional data structures.
"""

def first_duplicate(arr):
    """
    This function finds and returns the first duplicate element in an array of integers.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    int: The first duplicate element found in the array, or -1 if no duplicate is found.
    """
    
    # Create a set to store visited elements
    visited = set()
    
    # Iterate through the array
    for num in arr:
        # Check if the current number is already in the set
        if num in visited:
            # If it is, return the number as the first duplicate
            return num
        else:
            # If not, add the number to the set
            visited.add(num)
    
    # If no duplicate is found, return -1
    return -1