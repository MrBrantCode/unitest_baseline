"""
QUESTION:
Write a function `rotate_square_img_counter_clockwise(matrix)` that rotates a given square matrix 90 degrees counterclockwise in-place, i.e., without using any additional memory. The input matrix is a 2D list of integers and is guaranteed to be square (i.e., have the same number of rows and columns). The function should return the rotated matrix.
"""

def rotate_square_img_counter_clockwise(matrix):
    N = len(matrix)
    for x in range(N // 2):
        for y in range(x, N - x - 1):
            temp = matrix[x][y]
            
            # move values from right to top
            matrix[x][y] = matrix[y][N-1-x]
            
            # move values from bottom to right
            matrix[y][N-1-x] = matrix[N-1-x][N-1-y]
            
            # move values from left to bottom
            matrix[N-1-x][N-1-y] = matrix[N-1-y][x]
            
            # assign temp to left
            matrix[N-1-y][x] = temp

    return matrix