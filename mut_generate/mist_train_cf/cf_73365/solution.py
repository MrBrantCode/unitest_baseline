"""
QUESTION:
Write a function named `is_3d_array_sorted` that takes a 3D array as input. The function should verify if all elements in the 3D array are in ascending order depth-wise, row-wise, and column-wise. The 3D array is assumed to have the same length for each dimension.
"""

def is_3d_array_sorted(arr):
    # Verifying if the elements are in ascending order row-wise
    for mat in arr:
        for row in mat:
            if any(row[i] >= row[i + 1] for i in range(len(row) - 1)):
                return False

    # Verifying if the elements are in ascending order column-wise
    for mat in arr:
        for i in range(len(mat[0])):
            if any(mat[j][i] >= mat[j+1][i] for j in range(len(mat) - 1)):
                return False

    # Verifying if the elements are in ascending order depth-wise
    for i in range(len(arr[0])):
        for j in range(len(arr[0][0])):
            if any(arr[k][i][j] >= arr[k+1][i][j] for k in range(len(arr) - 1)):
                return False

    return True