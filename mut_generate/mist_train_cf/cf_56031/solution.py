"""
QUESTION:
Design a function `rotate3D(cube)` that takes a 3D cube as input, represented as a series of n x n 2D matrices, and returns the cube rotated 90 degrees around its central axis in a clockwise direction. The rotation should occur layer by layer, starting from the outermost layer inward. Implement the rotation without using any additional data structures beyond the input cube itself.
"""

def rotate(cube):
    n = len(cube)

    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # Save top
            top = cube[layer][i];

            # Move left to top
            cube[layer][i] = cube[last - i][layer];

            # Move bottom to left
            cube[last - i][layer] = cube[last][last - i]

            # Move right to bottom
            cube[last][last - i] = cube[i][last]

            # Move saved top to right
            cube[i][last] = top
    return cube