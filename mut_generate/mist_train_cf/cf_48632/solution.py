"""
QUESTION:
Write a function `is_sharpe_ratio_significant` that determines if the difference in Sharpe Ratio between two assets is significant. The function should take as input the Sharpe Ratios of Asset A and Asset B, and return a boolean indicating whether the difference is significant. Assume a 35% higher Sharpe Ratio is considered significant. The function should not consider any other factors or indicators, only the Sharpe Ratio values.
"""

def is_sharpe_ratio_significant(sharpe_ratio_a, sharpe_ratio_b):
    """
    Determines if the difference in Sharpe Ratio between two assets is significant.
    
    Args:
    sharpe_ratio_a (float): The Sharpe Ratio of Asset A.
    sharpe_ratio_b (float): The Sharpe Ratio of Asset B.
    
    Returns:
    bool: Whether the difference in Sharpe Ratio is significant (i.e., 35% higher).
    """
    return abs(sharpe_ratio_a - sharpe_ratio_b) / max(sharpe_ratio_a, sharpe_ratio_b) >= 0.35