"""
QUESTION:
Write a function `find_element(A, x)` that finds the position of element `x` in a given 2D array `A`. The function should return the position as a tuple `(i, j)` if `x` is found, where `i` is the row index and `j` is the column index. If `x` is not found in the array, the function should return -1.
"""

def find_element(A, x):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] == x:
                return (i, j)
    return -1