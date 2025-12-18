"""
QUESTION:
Write a function named `find_smallest_sum_row` that takes a list of rows as input, where each row is a tuple of four elements: `n`, `a_n`, `b_n`, and `c_n`. The function should calculate the sum of the squares of the differences between `a_n`, `b_n`, and `c_n` for each row, and return the value of `n` corresponding to the row with the smallest sum.
"""

def find_smallest_sum_row(rows):
    """
    Calculate the sum of the squares of the differences between a_n, b_n, and c_n for each row,
    and return the value of n corresponding to the row with the smallest sum.

    Args:
        rows (list): A list of rows, where each row is a tuple of four elements: n, a_n, b_n, and c_n.

    Returns:
        int: The value of n corresponding to the row with the smallest sum.
    """
    smallest_sum = float('inf')
    smallest_n = None
    for n, a_n, b_n, c_n in rows:
        sum_of_squares = (a_n - b_n)**2 + (a_n - c_n)**2 + (b_n - c_n)**2
        if sum_of_squares < smallest_sum:
            smallest_sum = sum_of_squares
            smallest_n = n
    return smallest_n