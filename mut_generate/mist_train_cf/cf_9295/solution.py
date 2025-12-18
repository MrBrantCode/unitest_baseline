"""
QUESTION:
Create a function named `allocateAndInitialize` that takes an integer `size` as input and returns a pointer to an array of integers. The function should dynamically allocate memory for the array and initialize all elements to 0. The function should handle memory allocation internally and return a pointer to the allocated array.
"""

def allocateAndInitialize(size):
    # Python does not support direct memory allocation like C++
    # Instead, we use a list to simulate the behavior
    arr = [0] * size  # initializing the list with zeros
    
    return arr