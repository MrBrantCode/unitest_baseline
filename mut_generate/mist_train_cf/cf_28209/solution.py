"""
QUESTION:
Implement a function `calculate_total_commission` that takes in a list of trade details, account type, capital base, commission structure, and slippage, and returns the total commission incurred for all the trades. The commission structure consists of a buy cost, sell cost, and unit, while the slippage includes a value and unit. Each trade is represented as a tuple containing the trade type ('buy' or 'sell') and trade value. The function should calculate the total commission based on the given commission structure and slippage, and return the result. 

The function signature should be `calculate_total_commission(trade_details, account_type, capital_base, commission, slippage)`.
"""

def calculate_total_commission(trade_details, account_type, capital_base, commission, slippage):
    """
    Calculate the total commission incurred for all trades.

    Parameters:
    trade_details (list): A list of tuples containing trade type ('buy' or 'sell') and trade value.
    account_type (str): The type of account.
    capital_base (float): The capital base.
    commission (dict): A dictionary containing buy cost, sell cost, and unit.
    slippage (dict): A dictionary containing value and unit.

    Returns:
    float: The total commission incurred for all trades.
    """
    total_commission = 0
    for trade_type, trade_value in trade_details:
        if trade_type == 'buy':
            total_commission += (trade_value * commission['buycost'] * commission['unit']) + (trade_value * slippage['value'] * slippage['unit'])
        elif trade_type == 'sell':
            total_commission += (trade_value * commission['sellcost'] * commission['unit']) + (trade_value * slippage['value'] * slippage['unit'])
    return total_commission