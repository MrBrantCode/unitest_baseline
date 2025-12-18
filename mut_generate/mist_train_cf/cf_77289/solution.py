"""
QUESTION:
Calculate the discount rate for a given zero coupon bond using the Bloomberg interest rate curve method. 

The discount rate should be calculated using the formula: Discount Factor = 1 / (1 + r/100) ^ t, where r is the zero rate from a zero coupon yield curve and t is the time to maturity in years. 

Implement a function named `calculate_discount_rate` that takes two parameters: `r` (the zero rate) and `t` (the time to maturity in years), and returns the corresponding discount rate.
"""

def calculate_discount_rate(r, t):
    """
    Calculate the discount rate for a given zero coupon bond using the Bloomberg interest rate curve method.

    Parameters:
    r (float): The zero rate from a zero coupon yield curve.
    t (float): The time to maturity in years.

    Returns:
    float: The corresponding discount rate.
    """
    return 1 / (1 + r/100) ** t