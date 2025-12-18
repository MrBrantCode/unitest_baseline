"""
QUESTION:
Design a function named `rotate` that rotates a given 2-D list (representing a matrix) by a specified number of clockwise 90-degree positions. The function should work for both square and rectangular matrices, and it should be able to handle any number of specified positions.
"""

def rotate(mat, positions):
    def rotate_once(mat):
        return [list(x)[::-1] for x in zip(*mat)]
    
    for _ in range(positions):
        mat = rotate_once(mat)
    return mat