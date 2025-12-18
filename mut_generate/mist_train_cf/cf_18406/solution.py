"""
QUESTION:
Write a function `calculateCompoundInterest` that takes four parameters: `principal`, `rate`, `time`, and `frequency`. The function should calculate the compound interest based on the given principal amount, interest rate, time period, and frequency of compounding. The frequency of compounding refers to the number of times the interest is compounded per year. Assume that the input values for `principal`, `rate`, `time`, and `frequency` will always be positive integers. The formula to calculate the compound interest is A = P(1 + r/n)^(nt), where A is the final amount, P is the principal amount, r is the annual interest rate (expressed as a decimal), n is the number of times that interest is compounded per year, and t is the time the money is invested for (in years).
"""

def calculateCompoundInterest(principal, rate, time, frequency):
    """
    Calculate the compound interest based on the given principal amount, interest rate, time period, and frequency of compounding.

    Args:
    principal (float): The principal amount.
    rate (float): The annual interest rate (expressed as a decimal).
    time (int): The time the money is invested for (in years).
    frequency (int): The number of times that interest is compounded per year.

    Returns:
    float: The compound interest.
    """
    return principal * (1 + rate / frequency) ** (frequency * time)