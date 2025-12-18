"""
QUESTION:
Write a function named `find_singleton_position` that takes an array of integers as input and returns the numerical position of the first singleton element present in the array. A singleton element is a number that appears only once in the array. The position is given in 0-based indexing.
"""

def find_singleton_position(arr):
    """
    Returns the numerical position of the first singleton element in the array.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        int: The 0-based position of the first singleton element, or -1 if no singleton exists.
    """
    frequency = {}
    
    # Count the frequency of each number in the array
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Find the first singleton element and return its position
    for i, num in enumerate(arr):
        if frequency[num] == 1:
            return i
    
    # Return -1 if no singleton element is found
    return -1