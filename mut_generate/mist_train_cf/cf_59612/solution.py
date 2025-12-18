"""
QUESTION:
Write a function `calculate_investment_values` that takes in the total portfolio value, dividend earnings of four companies, and their respective annual dividend yields, to calculate the precise value of the investments in each company by the end of the year, assuming the dividends are reinvested back into the respective companies. The function should return the values of the investments in each company at the end of the year.
"""

def calculate_investment_values(total_portfolio_value, dividend_earnings, annual_dividend_yields):
    """
    Calculate the precise value of the investments in each company by the end of the year,
    assuming the dividends are reinvested back into the respective companies.

    Args:
        total_portfolio_value (float): The total value of the portfolio.
        dividend_earnings (list): A list of dividend earnings of four companies.
        annual_dividend_yields (list): A list of annual dividend yields of four companies.

    Returns:
        list: A list of the values of the investments in each company at the end of the year.
    """
    
    # Initialize an empty list to store the investment values
    investment_values = []
    
    # Iterate over the dividend earnings and annual dividend yields
    for i in range(len(dividend_earnings)):
        # Calculate the initial investment value
        initial_investment_value = dividend_earnings[i] / annual_dividend_yields[i]
        
        # Calculate the investment value at the end of the year with reinvested dividends
        investment_value = initial_investment_value + initial_investment_value * annual_dividend_yields[i]
        
        # Append the investment value to the list
        investment_values.append(investment_value)
    
    # Return the list of investment values
    return investment_values