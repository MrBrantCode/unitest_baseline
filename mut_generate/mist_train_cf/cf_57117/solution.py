"""
QUESTION:
Design a function `calculate_sum` that calculates the accumulated sum of funds after a given period of years. The function should take four parameters: `base_sum` (initial amount of money), `interest_rate` (annual interest rate), `period` (number of years), and `compound_times` (number of times the interest is compounded per year, where 4 represents quarterly, 2 represents semi-annually, and 1 represents annually). The function should return the accumulated sum of funds after the period of years, handling floating-point precision errors that may arise from the calculations.
"""

from decimal import Decimal, getcontext

def calculate_sum(base_sum, interest_rate, period, compound_times):
    """
    Compute the final sum with compounded interest using a precise type Decimal
    :param base_sum: Initial amount of money
    :param interest_rate: Annual interest rate
    :param period: Number of years
    :param compound_times: Number of times the interest is compounded per year
    :return: Accumulated sum of funds after the period of years
    """
    
    # Set the precision for Decimal calculations
    getcontext().prec = 10

    # convert inputs to Decimal for precision
    base_sum = Decimal(base_sum)
    interest_rate = Decimal(interest_rate)
    period = Decimal(period)
    compound_times = Decimal(compound_times)

    accum_sum = base_sum * (1 + interest_rate / (100 * compound_times)) ** (compound_times * period)
    return float(accum_sum)