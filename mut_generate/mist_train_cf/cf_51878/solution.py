"""
QUESTION:
Find the feasible initial capital distribution for two investment schemes with a total of $1000. The first scheme returns 8% annually and the second returns 6%. No more than 60% of the total capital can be assigned to each scheme. The total return value after one year is $80.
"""

def entrance(capital, scheme1_rate, scheme2_rate, max_percentage, target_return):
    """
    Calculate the feasible initial capital distribution for two investment schemes.

    Args:
    capital (float): Total capital to be invested.
    scheme1_rate (float): Annual return rate of the first scheme.
    scheme2_rate (float): Annual return rate of the second scheme.
    max_percentage (float): Maximum percentage of capital that can be assigned to each scheme.
    target_return (float): Target return value after one year.

    Returns:
    float: Amount of capital to be invested in the first scheme.
    """
    max_investment = capital * max_percentage / 100
    for x in range(int(max_investment) + 1):
        if round(scheme1_rate * x + scheme2_rate * (capital - x), 2) == target_return:
            return x
    return None

# Removed test case for reorganization