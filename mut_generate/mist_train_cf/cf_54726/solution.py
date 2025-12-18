"""
QUESTION:
Create a function named `process_data` that takes a 4-dimensional array as input and returns the processed array, preserving the original array's state. The input array is a 4x4x4x4 numpy array. Ensure the function can handle the array efficiently and modify the array as needed, keeping in mind that numpy supports vectorized operations.
"""

import numpy as np

def process_data(data):
    # Expand your logic here to process the 4D array as per your requirement
    # This is a sample where each element of the 4D array is incremented by 1
    return data + 1