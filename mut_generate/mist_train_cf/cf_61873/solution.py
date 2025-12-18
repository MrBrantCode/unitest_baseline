"""
QUESTION:
Design a function `gbtc_premium_discount` that calculates the premium or discount of the GBTC (Grayscale Bitcoin) ETF given the ETF's NAV, the number of shares outstanding, and the market price of GBTC. The function should consider the closed-end structure of the fund, which prevents new shares from being created or redeemed on a daily basis.
"""

def gbtc_premium_discount(nav, shares_outstanding, market_price):
    """
    Calculate the premium or discount of the GBTC (Grayscale Bitcoin) ETF.

    Args:
    nav (float): The net asset value of the ETF.
    shares_outstanding (int): The number of shares outstanding.
    market_price (float): The market price of GBTC.

    Returns:
    float: The premium or discount of the GBTC ETF.
    """

    # Calculate the total NAV value
    total_nav = nav * shares_outstanding
    
    # Calculate the market capitalization
    market_cap = market_price * shares_outstanding
    
    # Calculate the premium or discount
    premium_discount = ((market_cap - total_nav) / total_nav) * 100
    
    return premium_discount