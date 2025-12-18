"""
QUESTION:
Create a function named `calculate_day_one_pnl` that calculates the Day 1 PnL and reserve for a derivative trade, taking into account the theoretical value and the price sold. The function should consider the risk profile of the derivative instrument and the entity's risk appetite and regulatory framework.
"""

def calculate_day_one_pnl(theoretical_value, price_sold):
    """
    Calculate the Day 1 PnL and reserve for a derivative trade.

    Args:
    theoretical_value (float): The theoretical value of the derivative.
    price_sold (float): The price at which the derivative was sold.

    Returns:
    tuple: A tuple containing the Day 1 PnL and reserve.
    """
    day_one_pnl = price_sold - theoretical_value
    # For simplicity, assume the reserve is a portion of the day_one_pnl
    # In practice, this would be determined by the institution's risk management policy
    reserve = day_one_pnl * 0.5  # 50% of day_one_pnl
    return day_one_pnl, reserve