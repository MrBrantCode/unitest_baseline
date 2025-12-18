"""
QUESTION:
Write a Python function `calculate_pascal_triangle` to generate Pascal's triangle up to a given number of rows. The function should take an integer `rows` as input, where `rows` must be a positive integer greater than zero. It should handle invalid input and return an error message. The function should calculate each number in the triangle using a recursive algorithm with memoization. The function should also calculate and return the sum of numbers in each row of the triangle.

The function should print the Pascal's triangle in a formatted manner, with each number aligned properly. It should also handle potential memory errors when calculating large Pascal's triangles and return an error message if the memory limit is reached.

The function should be optimized for performance and use mathematical formulas to calculate the sum of numbers in each row directly instead of using a loop.

The function should be implemented with a command-line interface, allowing the user to provide the number of rows as a command-line argument. The function should display the Pascal's triangle and the sum of numbers in each row directly in the terminal.

Note: The function should not take any additional arguments other than `rows`. All additional functionality should be implemented within the function or its helper functions.
"""

def calculate_pascal_triangle(rows):
    """
    Generate Pascal's triangle up to a given number of rows.

    Args:
        rows (int): The number of rows in the triangle.

    Returns:
        list: A 2D list representing the Pascal's triangle.

    Raises:
        MemoryError: If the memory limit is exceeded while calculating the triangle.
    """
    triangle = [[1] * (row + 1) for row in range(rows)]
    for row in range(rows):
        for col in range(1, row):
            triangle[row][col] = triangle[row-1][col-1] + triangle[row-1][col]
    return triangle