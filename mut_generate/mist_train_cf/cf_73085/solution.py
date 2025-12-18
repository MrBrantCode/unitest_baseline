"""
QUESTION:
Implement a function named `zigzagTraverse3D` to traverse a 3D matrix in a zigzag pattern. The zigzag pattern follows from left to right and then right to left based on the y-axis, and continues this pattern for each z dimension. The function should take a 3D matrix as input and return a one-dimensional list containing all elements in the zigzag order. The input 3D matrix is a list of lists of lists, where each inner list represents a row in the 2D matrix, and each 2D matrix is a layer in the 3D matrix.
"""

def zigzagTraverse3D(matrix):
    z_dim = len(matrix)
    y_dim = len(matrix[0])
    x_dim = len(matrix[0][0])
    result = []
    
    for z in range(z_dim):
        for y in range(y_dim):
            if y % 2 == 0:  # moving rightwards
                for x in range(x_dim):
                    result.append(matrix[z][y][x])
            else:  # moving leftwards
                for x in range(x_dim-1, -1, -1):
                    result.append(matrix[z][y][x])
                    
    return result