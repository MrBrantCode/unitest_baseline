"""
QUESTION:
Given two points A and B, where A is the optimal portfolio for a given utility function and B is the optimal attainable portfolio defined by the Capital Market Line (CML) when a risk-free asset is introduced, write a function called `compare_points_A_B` that determines under what conditions these two points are the same. Assume that the utility function's slope represents the investor's risk aversion level and the CML's slope represents the market's degree of risk aversion.
"""

def compare_points_A_B(utility_slope, market_slope):
    """
    Compare the slopes of the utility function and the Capital Market Line.

    Args:
        utility_slope (float): The slope of the utility function.
        market_slope (float): The slope of the Capital Market Line.

    Returns:
        bool: True if the two points are the same, False otherwise.
    """
    return utility_slope == market_slope