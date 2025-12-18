"""
QUESTION:
Create a function `calculate_forward_price` that takes in the spot price of XAU/USD, the annualized U.S. interest rate, and the annualized gold lease rate, and returns the forward price (swap rate) for a one-month period. The function should assume that the interest rates are annualized and need to be converted to a 1-month percentage rate. The calculation should use the formula: `Forward Price = Spot Price * (1 + U.S. 1-month rate - Gold 1-month lease rate)`.
"""

def calculate_forward_price(spot_price, us_interest_rate, gold_lease_rate):
    """
    Calculate the forward price (swap rate) for a one-month period.

    Parameters:
    spot_price (float): The spot price of XAU/USD.
    us_interest_rate (float): The annualized U.S. interest rate.
    gold_lease_rate (float): The annualized gold lease rate.

    Returns:
    float: The forward price (swap rate) for a one-month period.
    """
    # Convert interest rates from annual to 1-month percentage rate
    us_1_month_rate = us_interest_rate / 12
    gold_1_month_rate = gold_lease_rate / 12
    
    # Calculate the forward price
    forward_price = spot_price * (1 + us_1_month_rate - gold_1_month_rate)
    
    return forward_price