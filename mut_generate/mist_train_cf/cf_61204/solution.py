"""
QUESTION:
Construct a function `is_descending_3d_array` that checks if all the elements in a given 3D array are in descending order in terms of height (depth), row, and column. The function should take a 3D array as input, which is a list of lists of lists, and return True if all elements are in descending order, False otherwise. The function should consider an empty array or any array with empty dimensions as True.
"""

def is_descending_3d_array(arr):
    if not arr or not arr[0] or not arr[0][0]:
        return True

    depth = len(arr)
    rows = len(arr[0])
    cols = len(arr[0][0])

    for i in range(depth - 1):
        for j in range(rows):
            for k in range(cols):
                if arr[i][j][k] < arr[i+1][j][k]:
                    return False

    for i in range(depth):
        for j in range(rows - 1):
            for k in range(cols):
                if arr[i][j][k] < arr[i][j+1][k]:
                    return False

    for i in range(depth):
        for j in range(rows):
            for k in range(cols - 1):
                if arr[i][j][k] < arr[i][j][k+1]:
                    return False
                
    return True