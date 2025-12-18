"""
QUESTION:
Create a function `right_triangle(n: int)` that generates a right triangle using the '*' character of side length `n`. The function should return the triangle as a string, with each row on a new line. If `n` is less than or equal to 0, the function should return an error message.
"""

def entance(n: int) -> str:
    """
    Generates a right triangle using the '*' character of side length n.
    """
    if n <= 0:
        return "Error: Invalid input, N must be a positive integer."
    triangle = ""
    for i in range(1, n+1):
        triangle += "*"*i + "\n"
    return triangle