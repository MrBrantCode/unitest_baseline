"""
QUESTION:
Write a Python function called `calculate_correlation` that calculates the correlation between the returns of shares and bonds issued by the same issuer. The function should take two parameters: a list of share returns and a list of bond returns. It should return the correlation coefficient between the two lists of returns.
"""

import numpy as np

def calculate_correlation(share_returns, bond_returns):
    """
    Calculate the correlation coefficient between the returns of shares and bonds issued by the same issuer.

    Parameters:
    share_returns (list): A list of share returns
    bond_returns (list): A list of bond returns

    Returns:
    float: The correlation coefficient between the two lists of returns
    """
    return np.corrcoef(share_returns, bond_returns)[0, 1]