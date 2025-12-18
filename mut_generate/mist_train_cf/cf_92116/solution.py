"""
QUESTION:
Write a Python function named `transpose_array` that takes a 2D array of integers as input and returns its transposed version. The input array can contain integers ranging from -10^9 to 10^9. The function should return a new 2D array, without modifying the original input array.
"""

def entance(arr):
    rows = len(arr)
    cols = len(arr[0])
    
    # Create a new 2D array with transposed dimensions
    transposed_arr = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Traverse the original array and assign values to the transposed array
    for i in range(rows):
        for j in range(cols):
            transposed_arr[j][i] = arr[i][j]
    
    return transposed_arr