"""
QUESTION:
Create a function `calculate_client_spot` that takes the following parameters: `trader_spot`, `spot_markup`, `is_rhs_trade`, and `is_even_swap`. The function should return the `client_spot` rate based on the given conditions. The `client_spot` rate should be the `trader_spot` rate plus the `spot_markup` if `is_rhs_trade` is `True`, otherwise it should be the `trader_spot` rate minus the `spot_markup`. The function should handle both even and uneven swaps, but the treatment of the `spot_markup` should not differ between the two.
"""

def calculate_client_spot(trader_spot, spot_markup, is_rhs_trade, is_even_swap):
    if is_rhs_trade:
        client_spot = trader_spot + spot_markup
    else:
        client_spot = trader_spot - spot_markup
    return client_spot