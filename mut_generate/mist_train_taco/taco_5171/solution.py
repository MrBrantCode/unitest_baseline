"""
QUESTION:
Write a program which calculates the distance between two points P1(x1, y1) and P2(x2, y2).



Input

Four real numbers x1, y1, x2 and y2 are given in a line.

Output

Print the distance in real number. The output should not contain an absolute error greater than 10-4.

Example

Input

0 0 1 1


Output

1.41421356
"""

def calculate_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Calculate the distance between two points P1(x1, y1) and P2(x2, y2) in a 2D plane.

    Parameters:
    - x1 (float): The x-coordinate of the first point.
    - y1 (float): The y-coordinate of the first point.
    - x2 (float): The x-coordinate of the second point.
    - y2 (float): The y-coordinate of the second point.

    Returns:
    - float: The distance between the two points, with a precision of at least 10^-4.
    """
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distance