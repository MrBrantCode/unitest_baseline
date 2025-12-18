"""
QUESTION:
Write a function named `calculate_investments` that calculates the total amount invested in two funds with a 2% dividend yield and two funds with a 4% dividend yield, given the total investment of $5000 and total dividend of $150. The function should return the combined investment in the 2% funds and the combined investment in the 4% funds.
"""

def calculate_investments(total_investment, total_dividends, dividend_yield_fund1_fund2, dividend_yield_fund3_fund4):
    """
    Calculate the total amount invested in two funds with a 2% dividend yield and two funds with a 4% dividend yield.

    Args:
        total_investment (float): The total investment amount.
        total_dividends (float): The total dividend earned.
        dividend_yield_fund1_fund2 (float): The dividend yield for the first two funds.
        dividend_yield_fund3_fund4 (float): The dividend yield for the last two funds.

    Returns:
        tuple: A tuple containing the combined investment in the 2% funds and the combined investment in the 4% funds.
    """

    fund1_fund2_investment = (total_dividends - (total_investment * dividend_yield_fund3_fund4)) / (dividend_yield_fund1_fund2 - dividend_yield_fund3_fund4)
    fund3_fund4_investment = total_investment - fund1_fund2_investment

    return fund1_fund2_investment, fund3_fund4_investment