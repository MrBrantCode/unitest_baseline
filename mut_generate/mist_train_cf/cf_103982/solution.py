"""
QUESTION:
Write a function `rotate_array_clockwise` that takes a 2D square array of integers as input and returns the array rotated 90 degrees clockwise. The input array may contain duplicate values. The function should not modify the input array and should return a new array with the rotated values.
"""

def rotate_array_clockwise(array):
    n = len(array)
    rotated_array = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_array[j][n-1-i] = array[i][j]
    return rotated_array