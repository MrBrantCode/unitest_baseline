"""
QUESTION:
Write a function `longest_diagonal(cube, target)` that takes a 3D cube of non-negative integers and a target value as input, and returns the longest diagonal in the cube where the product of its elements equals the target value, along with the cube coordinates of the diagonal elements. The function should consider only diagonals that run parallel to the main diagonal of the cube.
"""

from collections import deque
import numpy as np

def longest_diagonal(cube, target):
    matrix = np.array(cube)
    queue = deque([(i, j, k) for i in range(len(matrix)) for j in range(len(matrix[0])) for k in range(len(matrix[0][0])) if matrix[i][j][k] == target])
    max_len = 0
    max_diagonal = []
    max_coordinates = []
    while queue:
        x, y, z = queue.popleft()
        diagonal, coordinates = get_diagonal(matrix, x, y, z)
        product = np.prod(diagonal)
        if product == target and len(diagonal) > max_len:
            max_len = len(diagonal)
            max_diagonal = diagonal
            max_coordinates = coordinates
    return max_diagonal, max_coordinates

def get_diagonal(matrix, x, y, z):
    diagonal = []
    coordinates = []
    while x < len(matrix) and y < len(matrix[0]) and z < len(matrix[0][0]):
        diagonal.append(matrix[x][y][z])
        coordinates.append((x, y, z))
        x += 1
        y += 1
        z += 1
    return diagonal, coordinates