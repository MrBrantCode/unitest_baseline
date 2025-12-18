"""
QUESTION:
Write a function named `calculate_degrees_of_freedom` that takes two parameters, `num_rows` and `num_cols`, representing the dimensions of a contingency table. The function should return the number of degrees of freedom for a chi-squared test of independence, calculated using the formula (R-1) * (C-1), where R is the number of rows and C is the number of columns.
"""

def calculate_degrees_of_freedom(num_rows, num_cols):
    """
    Calculate the number of degrees of freedom for a chi-squared test of independence.

    Args:
        num_rows (int): The number of rows in the contingency table.
        num_cols (int): The number of columns in the contingency table.

    Returns:
        int: The number of degrees of freedom.
    """
    return (num_rows - 1) * (num_cols - 1)