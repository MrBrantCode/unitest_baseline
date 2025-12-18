"""
QUESTION:
Write a function `generate_spiral_matrix` that generates an n x n matrix filled with numbers from 1 to n^2 in a clockwise spiral pattern. The function should return the generated matrix.

The matrix should start from the top left corner and move right, then down, then left, then up, and so on. If the next position is outside the matrix or has already been filled, the direction of movement should be changed accordingly. The function should be able to handle any positive integer n.
"""

def generate_spiral_matrix(n):
    """
    Generates an n x n matrix filled with numbers from 1 to n^2 in a clockwise spiral pattern.

    Args:
        n (int): The size of the matrix.

    Returns:
        list: A 2D list representing the generated matrix.
    """
    matrix = [[0] * n for _ in range(n)]
    x, y, dx, dy = 0, 0, 1, 0
    for i in range(n * n):
        matrix[y][x] = i + 1
        if x + dx == n or y + dy == n or matrix[y + dy][x + dx]:
            dx, dy = -dy, dx
        x, y = x + dx, y + dy
    return matrix