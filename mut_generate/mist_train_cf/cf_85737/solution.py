"""
QUESTION:
Write a function named 'calculate_NAV' that takes in two parameters: 'assets' and 'liabilities'. The function should calculate the Net Asset Value (NAV) by subtracting the liabilities from the assets and return the result. The 'assets' and 'liabilities' should be represented as numerical values, and the function should return a numerical value.
"""

def calculate_NAV(assets, liabilities):
    """
    Calculate the Net Asset Value (NAV) by subtracting liabilities from assets.

    Args:
    assets (float): The total value of assets.
    liabilities (float): The total value of liabilities.

    Returns:
    float: The calculated Net Asset Value (NAV).
    """
    return assets - liabilities