"""
QUESTION:
Write a function `calculate_future_price` that takes in the current spot price and carrying cost as parameters and returns the future price of a futures contract, considering the basic pricing model of futures price = spot price + carrying cost.
"""

def calculate_future_price(spot_price, carrying_cost):
    """
    This function calculates the future price of a futures contract based on the basic pricing model.
    
    Parameters:
    spot_price (float): The current spot price of the asset.
    carrying_cost (float): The carrying cost of the asset.
    
    Returns:
    float: The future price of the futures contract.
    """
    return spot_price + carrying_cost