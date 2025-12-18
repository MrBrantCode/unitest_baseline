"""
QUESTION:
Write a function `calculate_spread` that takes in the bond's price, dollar duration, bond's yield, and the yield of a comparable 'risk-free' bond. Use these inputs to calculate the spread of the bond, which is the difference between the bond's yield and the yield of the comparable 'risk-free' bond. Assume all yields are given in decimal form (i.e. 0.05 for 5%).
"""

def calculate_spread(bond_price, dollar_duration, bond_yield, risk_free_yield):
    """
    Calculate the spread of a bond, which is the difference between the bond's yield and the yield of a comparable 'risk-free' bond.

    Args:
    bond_price (float): The price of the bond.
    dollar_duration (float): The dollar duration of the bond.
    bond_yield (float): The yield of the bond in decimal form.
    risk_free_yield (float): The yield of a comparable 'risk-free' bond in decimal form.

    Returns:
    float: The spread of the bond.
    """
    # The spread is simply the difference between the bond's yield and the yield of the comparable 'risk-free' bond
    spread = bond_yield - risk_free_yield
    return spread