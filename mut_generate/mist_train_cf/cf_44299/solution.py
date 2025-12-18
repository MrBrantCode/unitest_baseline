"""
QUESTION:
Create a function named 'calculate_bond_price' that takes in the daily change of zero coupon spot rates and the daily change of z-spread for corporate bonds. The function should return the computed price of a bond using these changes.
"""

def calculate_bond_price(daily_change_spot_rate, daily_change_z_spread):
    """
    Compute the price of a bond using the daily change of zero coupon spot rates and the daily change of z-spread for corporate bonds.

    Args:
    - daily_change_spot_rate (float): The daily change of zero coupon spot rates.
    - daily_change_z_spread (float): The daily change of z-spread for corporate bonds.

    Returns:
    - float: The computed price of the bond.
    """
    # Assuming the bond price computation formula is P = 1 / (1 + daily_change_spot_rate + daily_change_z_spread)
    bond_price = 1 / (1 + daily_change_spot_rate + daily_change_z_spread)
    return bond_price