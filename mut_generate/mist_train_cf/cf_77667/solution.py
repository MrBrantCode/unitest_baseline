"""
QUESTION:
Create a function named `rotate_matrix` that takes a 2D list as input, rotates it 90 degrees clockwise, and prints the rotated matrix in a 2D format. The input matrix can be a rectangle, not necessarily a square.
"""

def rotate_matrix(matrix):
    return [[matrix[j][i] for j in reversed(range(len(matrix)))] for i in range(len(matrix[0]))]