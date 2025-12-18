"""
QUESTION:
Write a function named `copy_array` that takes an array of integers as input, creates a copy of the array without using any built-in array copying functions or methods, and returns the copied array. The function should optimize the copying process to minimize the time complexity for large array sizes (10^6 to 10^7).
"""

def copy_array(original_array):
    # Preallocate the new array with the same size as the original array
    copied_array = [0] * len(original_array)

    # Iterate through each index of the original array
    for i in range(len(original_array)):
        # Copy the element at index 'i' to the new array at the same index
        copied_array[i] = original_array[i]

    # Return the copied array
    return copied_array