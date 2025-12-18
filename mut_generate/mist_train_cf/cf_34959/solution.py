"""
QUESTION:
Implement the `rebalance` function, which takes in four parameters: `krypfolio` (a dictionary representing the current state of the investment portfolio), `prices` (a dictionary of cryptocurrency prices), `alloc` (a dictionary of allocation percentages), and `investment` (the total investment amount). 

The function should calculate the target allocation amount for each cryptocurrency based on the total investment amount and the specified allocation percentages. It should then compare the current allocation with the target allocation for each cryptocurrency and determine the necessary adjustments. Finally, it should buy or sell cryptocurrencies to rebalance the portfolio according to the allocation strategy and return the updated state of the investment portfolio after rebalancing. 

Assume that the `krypfolio` dictionary maps cryptocurrency names to the amount of each cryptocurrency in the portfolio, the `prices` dictionary maps cryptocurrency names to their prices, and the `alloc` dictionary maps cryptocurrency names to their allocation percentages.
"""

def rebalance(krypfolio, prices, alloc, investment):
    """
    Rebalance the investment portfolio according to the specified allocation strategy.

    Args:
    krypfolio (dict): Current state of the investment portfolio.
    prices (dict): Dictionary of cryptocurrency prices.
    alloc (dict): Dictionary of allocation percentages.
    investment (float): Total investment amount.

    Returns:
    dict: Updated state of the investment portfolio after rebalancing.
    """
    target_alloc = {crypto: investment * percentage / 100 for crypto, percentage in alloc.items()}
    
    for crypto, target_amount in target_alloc.items():
        current_amount = krypfolio.get(crypto, 0)
        target_diff = target_amount - current_amount * prices[crypto]
        if target_diff > 0:  # Buy more of the cryptocurrency
            buy_amount = min(target_diff, investment)
            if buy_amount > 0:
                krypfolio[crypto] = current_amount + buy_amount / prices[crypto]
                investment -= buy_amount
        elif target_diff < 0:  # Sell some of the cryptocurrency
            sell_amount = min(-target_diff, current_amount * prices[crypto])
            if sell_amount > 0:
                krypfolio[crypto] = current_amount - sell_amount / prices[crypto]
                investment += sell_amount
        
    return krypfolio