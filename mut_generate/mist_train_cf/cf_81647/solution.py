"""
QUESTION:
Design a function called `rotateCube` that takes a 3D cube represented as a series of 2D matrices as input and returns the rotated cube 90 degrees around its central axis. The rotation should occur layer by layer, starting from the outermost layer inward. The input cube is a list of 2D lists of integers, and the output should be in the same format. Each 2D matrix in the cube is a square matrix (i.e., it has the same number of rows and columns). The function should not modify the input cube.
"""

def rotateCube(cube):
    def rotateMatrix(matrix):
        result = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                result[j][-(i+1)] = val
        return result

    dim = len(cube)
    return [rotateMatrix(layer) for layer in cube]