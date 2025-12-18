"""
QUESTION:
Write a function named calculate_monthly_payment that calculates the monthly payment for a loan. The function should take three parameters: the loan amount (p), the annual interest rate (r) as a percentage, and the number of years (n) for the repayment period. The interest rate should be divided by 12 to get the monthly rate and the number of years should be multiplied by 12 to get the number of months. The function should return the monthly payment.
"""

def calculate_monthly_payment(p, r, n):
    """
    Calculate the monthly payment for a loan.

    Args:
        p (float): The loan amount.
        r (float): The annual interest rate as a percentage.
        n (float): The number of years for the repayment period.

    Returns:
        float: The monthly payment.
    """
    rate = (p * (r/1200)) / (1 - (1 + (r/1200))**(-n*12))
    return rate