"""
QUESTION:
Write a function `sum_3d_matrix(arr)` that calculates the sum of all values in a three-dimensional array `arr`, where `arr` can have different dimensional lengths. The function should handle cases where arrays within the matrix are not of uniform dimension by catching the TypeError exception and printing an error message.
"""

def sum_3d_matrix(arr):
    total_sum = 0
    try:
        for subarray_1 in arr:
            for subarray_2 in subarray_1:
                total_sum += sum(subarray_2)
    except TypeError:
        print("Array is irregular. Please ensure all arrays have the same dimensions.")
    return total_sum