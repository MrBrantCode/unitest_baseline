"""
QUESTION:
Calculate the Profit & Loss (P&L) of an existing FX Swap with a settled spot leg. The function should determine whether both the spot and forward legs are marked-to-market to the current spot rate or only the forward leg's NPV is considered.

Write a function named `calculate_fx_swap_pl` that takes into account the current spot rate and the forward leg's details to calculate the P&L.
"""

def calculate_fx_swap_pl(current_spot_rate, forward_leg_details):
    """
    Calculate the Profit & Loss (P&L) of an existing FX Swap with a settled spot leg.

    Args:
        current_spot_rate (float): The current spot rate.
        forward_leg_details (dict): A dictionary containing the forward leg's details, 
            including the strike rate, notional amount, and settlement date.

    Returns:
        float: The P&L of the FX Swap.
    """
    
    # Extract the forward leg details
    strike_rate = forward_leg_details['strike_rate']
    notional_amount = forward_leg_details['notional_amount']
    settlement_date = forward_leg_details['settlement_date']

    # Calculate the forward rate (assuming it's provided or can be calculated)
    # For simplicity, let's assume it's provided in the forward_leg_details
    forward_rate = forward_leg_details['forward_rate']

    # Calculate the NPV of the forward leg
    # This is a simplified example and actual NPV calculation may be more complex
    npv = notional_amount * (forward_rate - strike_rate)

    # The P&L is the NPV of the forward leg
    pl = npv

    return pl