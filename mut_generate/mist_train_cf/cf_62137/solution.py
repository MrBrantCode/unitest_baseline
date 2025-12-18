"""
QUESTION:
Write a function `calculate_df` that takes as input the number of internal knots `N` and the order of the polynomial `k` and returns the degrees of freedom `df` needed to fit a cubic spline curve. Assume the function will be used with a cubic spline, where `k` is 4 by default. The function should not take any other parameters.
"""

def calculate_df(N, k=4):
    """
    Calculate the degrees of freedom needed to fit a cubic spline curve.

    Parameters:
    N (int): The number of internal knots.
    k (int, optional): The order of the polynomial. Defaults to 4 for cubic spline.

    Returns:
    int: The degrees of freedom.
    """
    return N + k