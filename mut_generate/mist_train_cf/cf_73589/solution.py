"""
QUESTION:
Write a function `calculate_interest` that calculates the interest income or expense of a hedged call position in the Black-Scholes model. The function should take in the current price of the call option `C`, the underlying stock price `S`, the hedge ratio `Delta`, and the risk-free interest rate `r`. The function should return the interest income or expense over a small time period `dt`. The interest rate is continuously compounded.
"""

def calculate_interest(C, S, Delta, r, dt):
    """
    Calculate the interest income or expense of a hedged call position in the Black-Scholes model.

    Args:
    C (float): The current price of the call option.
    S (float): The underlying stock price.
    Delta (float): The hedge ratio.
    r (float): The risk-free interest rate.
    dt (float): A small time period.

    Returns:
    float: The interest income or expense.
    """
    return r * (C - Delta * S) * dt