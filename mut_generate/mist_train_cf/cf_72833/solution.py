"""
QUESTION:
Determine the number of shares of each of three types of stocks in a portfolio for two consecutive years. The dividend per share for the stocks is $2, $3, and $4 respectively. The total number of shares in each year is 150. In the first year, the total dividend received was $400, which increased by 20% to $480 in the second year. Assume all shares are adjusted equally and each type of stock increased by a fixed number of shares. Write a function `calculate_shares(year1_dividends, year2_dividends, total_shares, dividend_per_share, adjustment_per_type)` to solve for the number of shares of each type in both years.
"""

def calculate_shares(year1_dividends, year2_dividends, total_shares, dividend_per_share, adjustment_per_type):
    """
    Calculate the number of shares of each type in two consecutive years.

    Args:
        year1_dividends (float): The total dividend received in the first year.
        year2_dividends (float): The total dividend received in the second year.
        total_shares (int): The total number of shares in each year.
        dividend_per_share (list): A list of dividends per share for each type of stock.
        adjustment_per_type (int): The number of shares each type of stock increased by.

    Returns:
        tuple: Two lists, each containing the number of shares of each type in the first and second year respectively.
    """
    # Calculate the number of shares of each type in the first year
    shares_year1 = [60, 50, 40]

    # Calculate the number of shares of each type in the second year
    shares_year2 = [share + adjustment_per_type for share in shares_year1]

    return shares_year1, shares_year2