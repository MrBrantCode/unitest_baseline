"""
QUESTION:
Write a function `calculate_pnl` to calculate the profit and loss (PnL) for an Overnight Indexed Swap (OIS) trade. The function should take in the following parameters: the notional amount, the received rate, the pay rate, the start date of the unwind period, and the maturity date. The function should return the PnL in the currency of the notional amount. Assume a simplified case where daily resets are not considered.
"""

def calculate_pnl(notional_amount, received_rate, pay_rate, start_date, maturity_date):
    """
    Calculate the profit and loss (PnL) for an Overnight Indexed Swap (OIS) trade.

    Args:
        notional_amount (float): The notional amount of the swap.
        received_rate (float): The received rate of the swap.
        pay_rate (float): The pay rate of the swap.
        start_date (datetime): The start date of the unwind period.
        maturity_date (datetime): The maturity date of the swap.

    Returns:
        float: The PnL in the currency of the notional amount.
    """

    # Calculate the time in the contract in days
    time_in_contract = (maturity_date - start_date).days

    # Calculate the PnL using a simplified formula (daily resets not considered)
    pnl = (received_rate - pay_rate) * notional_amount * (time_in_contract / 360)

    return pnl