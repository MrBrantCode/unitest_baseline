"""
QUESTION:
Write a function `discount_factor` that calculates the discount factor for a cash flow with a specified number of years, risk-free rate, and credit spread. The function should not explicitly include the inflation rate in the calculation, as it is implicitly included in the risk-free rate.

The function should take three parameters: the number of years until the cash flow, the risk-free rate, and the credit spread. The risk-free rate and credit spread should be expressed as decimal values. The function should return the discount factor as a decimal value.
"""

def discount_factor(years, risk_free_rate, credit_spread):
    """
    Calculate the discount factor for a cash flow.

    Parameters:
    years (int): The number of years until the cash flow.
    risk_free_rate (float): The risk-free rate as a decimal value.
    credit_spread (float): The credit spread as a decimal value.

    Returns:
    float: The discount factor as a decimal value.
    """
    return (1 / (1 + risk_free_rate + credit_spread)) ** years