"""
QUESTION:
Write a function called `transpose_array` that takes a 2D array `arr` as input, where each inner array has the same length, and returns the transposed array by swapping the rows and columns of the original array. The input array can be of any size, but it must be a rectangular array (i.e., all inner arrays must have the same length).
"""

def transpose_array(arr):
    transposed_array = []
    
    for col in range(len(arr[0])):
        transposed_row = []
        for row in range(len(arr)):
            transposed_row.append(arr[row][col])
        transposed_array.append(transposed_row)
    
    return transposed_array