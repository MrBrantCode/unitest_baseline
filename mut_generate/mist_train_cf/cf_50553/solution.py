"""
QUESTION:
Calculate the change in value for each bond given the duration, change in credit spread, and optionally the initial bond price. The change should be approximated using a formula that assumes a small change in spread and uses duration as a linear approximation of the bond price's sensitivity to changes in spread. The function should be named `approximate_bond_value_change` and take the duration, change in spread, and initial bond price as parameters. The initial bond price is optional and if provided, should be used in the calculation.
"""

def approximate_bond_value_change(duration, change_in_spread, initial_bond_price=1):
    """
    Approximate the change in bond value given the duration, change in credit spread, 
    and optionally the initial bond price.

    Args:
    - duration (float): The sensitivity of a bond's price to changes in interest rates.
    - change_in_spread (float): The bond's spread change.
    - initial_bond_price (float, optional): The bond's initial price. Defaults to 1.

    Returns:
    - float: The approximate change in bond value.
    """
    return -duration * change_in_spread * initial_bond_price