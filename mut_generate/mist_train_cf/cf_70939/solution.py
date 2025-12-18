"""
QUESTION:
Write a function `calculate_investment_return` that takes in the following parameters: 
- `principal`: the initial investment amount
- `coupon_rate`: the annual coupon rate of the bond
- `yield_rate`: the annual yield rate of the bond
- `maturity`: the number of years until the bond matures
- `time_period`: the time period for which the interest rate changes
- `new_yield_rate`: the new yield rate after the interest rate change
- `macaulay_duration`: the Macaulay duration of the bond

Calculate the price risk and the reinvestment risk, and determine if the total return on investment is approximately the same at the end of the investment horizon, which is equal to the Macaulay duration of the bond.
"""

def calculate_investment_return(principal, coupon_rate, yield_rate, maturity, time_period, new_yield_rate, macaulay_duration):
    """
    Calculate the price risk and the reinvestment risk.

    Args:
    - principal (float): the initial investment amount
    - coupon_rate (float): the annual coupon rate of the bond
    - yield_rate (float): the annual yield rate of the bond
    - maturity (int): the number of years until the bond matures
    - time_period (float): the time period for which the interest rate changes
    - new_yield_rate (float): the new yield rate after the interest rate change
    - macaulay_duration (float): the Macaulay duration of the bond

    Returns:
    - price_risk (float): the price risk
    - reinvestment_risk (float): the reinvestment risk
    """

    # Calculate the initial present value
    present_value = sum([coupon_rate * principal / (1 + yield_rate) ** year for year in range(1, maturity + 1)]) + principal / (1 + yield_rate) ** maturity
    
    # Calculate the new present value after the interest rate change
    new_present_value = sum([coupon_rate * principal / (1 + new_yield_rate) ** year for year in range(1, maturity + 1)]) + principal / (1 + new_yield_rate) ** maturity
    
    # Calculate the price risk
    price_risk = present_value - new_present_value
    
    # Calculate the reinvestment risk
    reinvestment_risk = coupon_rate * principal * (1 + new_yield_rate) ** (macaulay_duration - time_period) - coupon_rate * principal
    
    return price_risk, reinvestment_risk