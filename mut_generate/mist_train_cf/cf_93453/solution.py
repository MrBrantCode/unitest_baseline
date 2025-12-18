"""
QUESTION:
Write a function `rotate_array_clockwise` that takes a 2D array of size n x n as input, and returns the array rotated 90 degrees clockwise. The array may contain duplicate values. The input array is a list of lists where each inner list has the same length, and the function should return a new rotated 2D array.
"""

def rotate_array_clockwise(array):
    n = len(array)
    rotated_array = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            rotated_array[j][n-1-i] = array[i][j]
    
    return rotated_array