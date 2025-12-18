"""
QUESTION:
Prove that the forward price of an asset, denoted as $F_{(t, T )}[S]$, is equal to the current price of the asset $S_t$ divided by the price of a zero-coupon bond $P(t,T)$, i.e., $F_{(t, T )}[S] =\frac{S_t}{P(t,T)}$.
"""

def calculate_forward_price(asset_price, zero_coupon_bond_price):
    """
    Calculate the forward price of an asset.

    Args:
    asset_price (float): The current price of the asset.
    zero_coupon_bond_price (float): The price of a zero-coupon bond.

    Returns:
    float: The forward price of the asset.
    """
    return asset_price / zero_coupon_bond_price