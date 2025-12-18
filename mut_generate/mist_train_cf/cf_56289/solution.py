"""
QUESTION:
Write a function named `discount_bond` that determines whether the spot rates from a given par swap curve can be used to discount the cash flows of a fixed-rate bond. The function should consider the type of bond (e.g., corporate, government) and the underlying asset of the par swap curve, and return a boolean indicating whether the spot rates can be used or if a specific yield curve for the bond is required.
"""

def discount_bond(bond_type, swap_curve_underlying):
    """
    Determines whether the spot rates from a given par swap curve can be used to discount the cash flows of a fixed-rate bond.

    Args:
    bond_type (str): The type of bond (e.g., corporate, government)
    swap_curve_underlying (str): The underlying asset of the par swap curve

    Returns:
    bool: Whether the spot rates can be used or if a specific yield curve for the bond is required
    """
    # In general, the spot rates can be used to discount the bond cash flows
    # However, if the bond has a different risk profile than the underlying of the swap, 
    # it might be more accurate to use a yield curve specific to that kind of bond
    if bond_type == swap_curve_underlying:
        return True
    else:
        return False