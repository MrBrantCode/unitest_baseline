"""
QUESTION:
Create a function called `reshape_array` that takes a 2D array as input and returns a reshaped array of shape (6,6). The reshaped array should be filled with the values from the original array, repeating them as necessary.
"""

import numpy as np

def reshape_array(arr):
    """
    Reshape a 2D array into a shape of (6,6) by repeating the original values as necessary.
    
    Parameters:
    arr (numpy.ndarray): The input 2D array.
    
    Returns:
    numpy.ndarray: The reshaped array of shape (6,6).
    """
    # Calculate the number of times the original array needs to be repeated
    repeat_times = int(np.ceil(6 * 6 / arr.size))
    
    # Repeat the original array
    repeated_array = np.tile(arr, repeat_times)
    
    # Reshape the repeated array
    reshaped_array = np.reshape(repeated_array, (6, 6))
    
    return reshaped_array