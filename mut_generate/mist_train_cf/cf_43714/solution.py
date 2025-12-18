"""
QUESTION:
Write a function `calculate_investment(total_investment, total_assets, stock_growth1, stock_growth2)` that calculates the amount invested in two stocks with annual growth rates `stock_growth1` and `stock_growth2`. The total initial investment is `total_investment`, and the total assets after one year is `total_assets`. The function should return the initial investments in each stock, assuming the investment is distributed dynamically based on the monthly performance of each stock, and the growth rates are achieved evenly over the year. 

Note: The growth rates are in percentage and should be used as decimals in calculations (i.e., 15% should be used as 0.15). However, they are given as percentages in the function parameters.
"""

def calculate_investment(total_investment, total_assets, stock_growth1, stock_growth2):
    """
    Calculate the initial investments in two stocks based on their growth rates.

    Args:
    total_investment (float): The total initial investment.
    total_assets (float): The total assets after one year.
    stock_growth1 (float): The annual growth rate of the first stock in percentage.
    stock_growth2 (float): The annual growth rate of the second stock in percentage.

    Returns:
    tuple: A tuple containing the initial investments in each stock.
    """
    stock_growth1 = stock_growth1 / 100  # Convert percentage to decimal
    stock_growth2 = stock_growth2 / 100  # Convert percentage to decimal
    investment1 = total_investment * stock_growth1 / (stock_growth1 + stock_growth2)
    investment2 = total_investment * stock_growth2 / (stock_growth1 + stock_growth2)
    return investment1, investment2