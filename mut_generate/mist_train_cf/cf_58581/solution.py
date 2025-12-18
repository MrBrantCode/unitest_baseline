"""
QUESTION:
Develop a function named `cross_product` that takes two 3D vectors represented as lists of three numbers each as input and returns their cross product as a list of three numbers. The input lists must be of length 3, and the function should not validate the input lengths.
"""

def cross_product(vector1, vector2):
    """
    Calculate the cross product of two 3D vectors.

    Args:
        vector1 (list): The first 3D vector.
        vector2 (list): The second 3D vector.

    Returns:
        list: The cross product of the two input vectors.
    """
    return [vector1[1]*vector2[2] - vector1[2]*vector2[1],
            vector1[2]*vector2[0] - vector1[0]*vector2[2],
            vector1[0]*vector2[1] - vector1[1]*vector2[0]]