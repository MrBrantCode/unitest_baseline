"""
QUESTION:
Write a function named `calculate_final_amount` that calculates the final amount after a given number of years with compound interest and inflation. The function should take in the principal amount, annual interest rate (as a decimal), inflation rate (as a decimal), number of times interest is compounded per year, and number of years as parameters. The function should return the final amount.
"""

def calculate_final_amount(principal, annual_interest_rate, inflation_rate, compound_frequency, years):
    return principal * (1 + (annual_interest_rate - inflation_rate)/compound_frequency) ** (compound_frequency*years)