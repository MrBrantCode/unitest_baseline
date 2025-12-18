"""
QUESTION:
Write a function `series_sum` to calculate the sum of the series n^4/(4n+2). The function should take an integer `n` as input, representing the number of terms to sum in the series.
"""

def series_sum(n):
    """
    Calculate the sum of the series n^4/(4n+2) up to n terms.
    
    Args:
    n (int): The number of terms to sum in the series.
    
    Returns:
    float: The sum of the series.
    """
    return sum(i**4 / (4*i + 2) for i in range(1, n + 1))