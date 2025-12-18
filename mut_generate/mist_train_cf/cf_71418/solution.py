"""
QUESTION:
Write a function `optimal_rebalancing_frequency` that determines the optimal rebalancing frequency given a forecast horizon and various market conditions, considering factors such as transaction costs, market volatility, and trading strategy. The function should take into account the potential benefits of rebalancing, including improved returns and reduced risk, and return the optimal frequency. The function should also consider that the forecast horizon may not always dictate the optimal rebalancing frequency, as market conditions can change.
"""

def optimal_rebalancing_frequency(forecast_horizon, transaction_costs, market_volatility, trading_strategy):
    """
    Determine the optimal rebalancing frequency given a forecast horizon and various market conditions.

    Parameters:
    forecast_horizon (int): The time period for which the forecast is made.
    transaction_costs (float): The costs associated with rebalancing.
    market_volatility (float): The volatility of the market.
    trading_strategy (str): The strategy employed for trading.

    Returns:
    str: The optimal rebalancing frequency.
    """
    # Consider the potential benefits of rebalancing, including improved returns and reduced risk
    # Simulate and backtest different rebalancing frequencies with the chosen strategy
    # Decide on the one that results in the highest risk-adjusted returns after taking into account transaction costs

    # For demonstration purposes, a simple example is provided
    if transaction_costs > 0.1 and market_volatility < 0.5:
        return "Monthly"
    elif trading_strategy == "aggressive" and market_volatility > 1.0:
        return "Daily"
    else:
        return "Weekly"