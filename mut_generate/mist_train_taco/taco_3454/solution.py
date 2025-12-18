"""
QUESTION:
Write a program which calculates the area and perimeter of a given rectangle.

Constraints

* 1 ≤ a, b ≤ 100

Input

The length a and breadth b of the rectangle are given in a line separated by a single space.

Output

Print the area and perimeter of the rectangle in a line. The two integers should be separated by a single space.

Example

Input

3 5


Output

15 16
"""

def calculate_rectangle_properties(a: int, b: int) -> tuple:
    """
    Calculate the area and perimeter of a rectangle given its length and breadth.

    Parameters:
    a (int): The length of the rectangle.
    b (int): The breadth of the rectangle.

    Returns:
    tuple: A tuple containing the area and perimeter of the rectangle.
    """
    area = a * b
    perimeter = 2 * (a + b)
    return (area, perimeter)