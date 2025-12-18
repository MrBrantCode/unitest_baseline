"""
QUESTION:
Create a function `calculateLoanPayment` that calculates the monthly loan payment based on the given parameters: loan amount, loan tenure, annual interest rate, and loan type. The function should handle both fixed and variable interest rates and accommodate extra payments or rate changes during the loan tenure. The interest rate should be converted from annual to monthly. The formula to calculate the loan payment is P = [r*PV] / [1 - (1 + r)^-n], where P is the monthly payment, r is the monthly interest rate, PV is the loan amount, and n is the number of payments.
"""

def calculateLoanPayment(loanAmount, tenure, annualInterestRate):
    """
    Calculate the monthly loan payment based on the given parameters.

    Args:
    loanAmount (float): The initial loan amount.
    tenure (int): The loan tenure in years.
    annualInterestRate (float): The annual interest rate.

    Returns:
    float: The monthly loan payment.
    """

    # Convert annual interest rate to monthly
    monthlyInterestRate = (annualInterestRate / 100) / 12

    # Calculate the number of payments
    numberOfPayments = tenure * 12

    # Calculate the loan payment using the formula
    monthlyPayment = (monthlyInterestRate * loanAmount) / (1 - (1 + monthlyInterestRate)**(-numberOfPayments))

    return monthlyPayment