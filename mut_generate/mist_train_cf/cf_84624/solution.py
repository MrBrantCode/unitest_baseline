"""
QUESTION:
Write a function `calculate_total_chairs` that calculates the total number of chairs set up for a meeting after adding more chairs to each row. The function should take three parameters: `num_rows`, `initial_chairs_per_row`, and `additional_chairs_per_row`. It should return the new total number of chairs. Assume that `num_rows` and `initial_chairs_per_row` are non-negative integers, and `additional_chairs_per_row` is a non-negative integer.
"""

def calculate_total_chairs(num_rows, initial_chairs_per_row, additional_chairs_per_row):
    """
    Calculate the total number of chairs after adding more chairs to each row.

    Args:
        num_rows (int): The number of rows.
        initial_chairs_per_row (int): The initial number of chairs per row.
        additional_chairs_per_row (int): The number of additional chairs per row.

    Returns:
        int: The new total number of chairs.
    """
    initial_total_chairs = num_rows * initial_chairs_per_row
    additional_chairs = num_rows * additional_chairs_per_row
    new_total_chairs = initial_total_chairs + additional_chairs
    return new_total_chairs