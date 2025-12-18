"""
QUESTION:
Create a function `triangle_square_sum(n)` that calculates the sum of the Triangle Series and the sum of the square of each number in the Triangle Series up to a given positive integer `n`. The function should handle large inputs efficiently and include error handling for invalid inputs, such as non-integer or non-positive values.
"""

def triangle_square_sum(n):
    """
    Function to calculate the sum of the Triangle Series and the sum of the square of each
    number in the Triangle Series up to n.
    """
    # error handling: if n is negative or not an integer
    if not isinstance(n, int) or n < 1:
        return "Error: Input must be an positive integer"

    # calculate the sum of the Triangle Series
    # formula for the sum of the first n natural numbers is n*(n+1)/2
    triangle_sum = n * (n + 1) // 2  # use integer division to ensure result is an integer

    # calculate the sum of the square of each number in the Triangle Series up to n.
    # formula for the sum of the squares of the first n natural numbers is n*(n+1)*(2n+1)/6
    square_sum = n * (n + 1) * (2 * n + 1) // 6  # use integer division to ensure result is an integer

    return triangle_sum, square_sum