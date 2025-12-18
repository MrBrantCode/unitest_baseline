"""
QUESTION:
Create a function `embed_value_3D_matrix(matrix, value, coordinates)` that embeds a given value at a specified coordinate position in a 3D matrix. The function should take as input a 3D matrix, a value, and a tuple of coordinates (x, y, z) where the value should be embedded. The function should return the updated matrix if the coordinates are within the matrix dimensions, and print an error message if the coordinates are out of bounds.
"""

def embed_value_3D_matrix(matrix, value, coordinates):
    x, y, z = coordinates
    if (x < len(matrix)) and (y < len(matrix[0])) and (z < len(matrix[0][0])):
        matrix[x][y][z] = value
    else:
        print("Coordinates are out of matrix dimensions")
    return matrix