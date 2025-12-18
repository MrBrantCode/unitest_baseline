"""
QUESTION:
Write a function called `constant_maturity_rolling` that takes a list of dates, a list of contract schedules/maturities, and a constant maturity as input. The function should return a list of adjusted contract schedules/maturities for each date, where the maturity is kept constant across each backtesting date by rolling the contract schedules/maturities backwards as you move backwards in time. Assume that the list of dates is in ascending order and the contract schedules/maturities are in the same order as the dates.
"""

def constant_maturity_rolling(dates, maturities, constant_maturity):
    """
    This function takes a list of dates, a list of contract schedules/maturities, 
    and a constant maturity as input. It returns a list of adjusted contract 
    schedules/maturities for each date, where the maturity is kept constant across 
    each backtesting date by rolling the contract schedules/maturities backwards 
    as you move backwards in time.

    Parameters:
    dates (list): A list of dates in ascending order.
    maturities (list): A list of contract schedules/maturities.
    constant_maturity (int): The constant maturity to be maintained.

    Returns:
    list: A list of adjusted contract schedules/maturities.
    """
    adjusted_maturities = []
    for i, date in enumerate(dates):
        adjusted_maturity = maturities[i] - (dates[-1] - date).days
        adjusted_maturities.append(max(adjusted_maturity, constant_maturity))
    return adjusted_maturities