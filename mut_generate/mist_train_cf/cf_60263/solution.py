"""
QUESTION:
Write a function named `printMulSquare` that takes an integer `dim` as input, representing the dimension of a multiplication square. The function should print the multiplication square in reverse order, starting from `dim*dim` down to 1, and store the results in a dictionary. The function should also be compatible with command line arguments for specifying the square dimensions. The dictionary should have tuples of the multiplication factors as keys and the product as values.
"""

def printMulSquare(dim):
    mulSquareDict = {}
    for i in reversed(range(1, dim+1)):
        for j in reversed(range(1, dim+1)):
            mulSquareDict[(i, j)] = i * j
            print(f"{i} * {j} = {i*j}")
    return mulSquareDict