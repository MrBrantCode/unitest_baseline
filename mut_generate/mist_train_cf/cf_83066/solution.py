"""
QUESTION:
Write a function `uncovered_interest_rate_parity` that takes two interest rates `r_USD` and `r_EUR` as inputs and returns the exchange rate `E_EUR,USD` according to the uncovered interest rate parity theory. Assume interest rates are given as decimal values. The function should calculate the exchange rate as (1+r_EUR)/(1+r_USD).
"""

def uncovered_interest_rate_parity(r_USD, r_EUR):
    """
    Calculate the exchange rate according to the uncovered interest rate parity theory.

    Args:
        r_USD (float): Interest rate in USD as a decimal value.
        r_EUR (float): Interest rate in EUR as a decimal value.

    Returns:
        float: The exchange rate E_EUR,USD.
    """
    return (1 + r_EUR) / (1 + r_USD)