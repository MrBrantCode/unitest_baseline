"""
QUESTION:
Calculate the dot product of two vectors. Create a function named `dot_product` that takes two lists of integers as input, representing the vectors, and returns their dot product. The function should multiply corresponding components of the vectors and add the products together. The vectors will be of equal length.
"""

def dot_product(vector1, vector2):
    """
    Calculate the dot product of two vectors.

    Args:
        vector1 (list): The first vector.
        vector2 (list): The second vector.

    Returns:
        int: The dot product of the two vectors.
    """
    return sum(a * b for a, b in zip(vector1, vector2))