"""
QUESTION:
Write a function called `relative_bos_spread_valuation` that determines whether a bond's bid-offer (BO) spread is too tight or too wide compared to its comparable bonds. The function should take in the bond's BO spread and a list of comparable bonds' BO spreads. The function should return a boolean indicating whether the bond's BO spread is in line with its peers.

Assume the BO spreads are provided by Bloomberg and BVAL (Bloomberg Valuation Service) and the comparable bonds are determined by their similar characteristics such as issuer, sector, rating, duration, and coupon.
"""

def relative_bos_spread_valuation(bond_bo_spread, comparable_bonds_bo_spreads):
    """
    This function determines whether a bond's bid-offer (BO) spread is too tight or too wide compared to its comparable bonds.

    Args:
    bond_bo_spread (float): The bond's BO spread.
    comparable_bonds_bo_spreads (list of floats): A list of comparable bonds' BO spreads.

    Returns:
    bool: A boolean indicating whether the bond's BO spread is in line with its peers.
    """
    # Calculate the average BO spread of the comparable bonds
    avg_comparable_bo_spread = sum(comparable_bonds_bo_spreads) / len(comparable_bonds_bo_spreads)

    # Define a tolerance level (e.g., 10%)
    tolerance_level = 0.1

    # Check if the bond's BO spread is within the tolerance level of the average comparable BO spread
    if (avg_comparable_bo_spread * (1 - tolerance_level)) <= bond_bo_spread <= (avg_comparable_bo_spread * (1 + tolerance_level)):
        return True  # The bond's BO spread is in line with its peers
    else:
        return False  # The bond's BO spread is not in line with its peers