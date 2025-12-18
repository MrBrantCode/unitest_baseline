"""
QUESTION:
Implement the `kelly_criterion_concurrent_bets` function. The function should calculate the optimal bet size for a new position when there are existing open positions. The bet size is calculated as a percentage of the total portfolio value, not just the remaining cash. Assume that the bets are independent of each other.
"""

def kelly_criterion_concurrent_bets(total_portfolio_value, bet_percentage):
    """
    Calculate the optimal bet size for a new position when there are existing open positions.
    
    Args:
    total_portfolio_value (float): The total value of the portfolio.
    bet_percentage (float): The desired percentage of the total portfolio to bet.
    
    Returns:
    float: The optimal bet size.
    """
    return total_portfolio_value * (bet_percentage / 100)