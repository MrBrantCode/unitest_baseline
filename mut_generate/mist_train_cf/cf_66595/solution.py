"""
QUESTION:
Implement a function named `spiralOrder` that takes a 2D list `matrix` as input and returns a list of elements in spiral order, starting from the top left corner and moving clockwise. The input matrix is a list of lists, where each inner list has the same length. The function should return a list of elements in spiral order.
"""

def spiralOrder(matrix):
    """
    Returns a list of elements in a 2D list in spiral order.

    Args:
        matrix (list): A 2D list of elements.

    Returns:
        list: A list of elements in spiral order.
    """
    res = []
    while matrix:
        res += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                res.append(row.pop())
        if matrix:
            res += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                res.append(row.pop(0))
    return res