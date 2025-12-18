"""
QUESTION:
Implement a function called `gittins_index` that calculates the Gittins Index for a given set of investment/trading strategies, assuming no cost in switching strategies, in order to determine the optimal strategy to maximize returns. The function should take into account the expected returns of each strategy, but not necessarily their risk.
"""

def gittins_index(strategy_returns):
    """
    Calculate the Gittins Index for a given set of investment/trading strategies.

    Parameters:
    strategy_returns (list): A list of expected returns for each strategy.

    Returns:
    list: A list of Gittins Index values corresponding to each strategy.
    """
    gittins_indexes = []
    
    # Calculate the Gittins Index for each strategy
    for i, return_rate in enumerate(strategy_returns):
        # Assuming discrete time intervals (e.g., days)
        # and no discounting for simplicity
        gittins_index = return_rate / (1 - return_rate)
        gittins_indexes.append(gittins_index)
    
    return gittins_indexes