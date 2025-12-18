"""
QUESTION:
Design a function `rotate_4D` that takes a 4D hypercube as input, where the hypercube is represented as a series of 3D cubes or arrays, each cube further divided into 2D matrices. The function should rotate the entire hypercube 90 degrees clockwise about its central axis. The rotation should occur layer by layer, starting from the outermost layer, moving inward.
"""

def rotate_4D(hypercube):
    size = len(hypercube)
    rotated = [[[['' for n in range(size)] for k in range(size)] for j in range(size)] for i in range(size)]

    for i in range(size):
        for j in range(size):
            for k in range(size):
                for n in range(size):
                    rotated[n][k][i][size - j - 1] = hypercube[i][j][k][n]

    return rotated