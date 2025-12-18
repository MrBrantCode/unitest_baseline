"""
QUESTION:
Create a function called `sortMultiArray` that takes a multi-dimensional array of integers as input and returns a one-dimensional sorted array in decreasing order, considering all values from the input matrix regardless of their original sub-array positions. The function should work with arbitrarily large matrices and handle negative integers and zero.
"""

def sortMultiArray(multi_array):
    # Flattening the multi-dimensional array to a one-dimensional array
    flat_array = [i for sublist in multi_array for i in sublist]
    
    # Sorting the flattened array in decreasing order
    sorted_array = sorted(flat_array, reverse=True)

    return sorted_array