"""
QUESTION:
Write a function called `transpose` that takes a two-dimensional array as input and returns its transpose, where the element at position (i, j) in the original matrix becomes the element at position (j, i) in the transposed matrix. The input array is assumed to be rectangular (i.e., all rows have the same number of columns).
"""

def transpose(arr):
    rows = len(arr)
    cols = len(arr[0])
    
    transposed_arr = [[0] * rows for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed_arr[j][i] = arr[i][j]
    
    return transposed_arr