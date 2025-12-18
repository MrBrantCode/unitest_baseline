"""
QUESTION:
Design a function named `calculate_continuous_compound_interest` that calculates the total accumulation of principal including interest based on continuous compounding. The function should take three parameters: the original principal sum `P`, the annual interest rate `r` as a decimal, and the number of years `t`.
"""

import math

def calculate_continuous_compound_interest(P, r, t):
    """
    Function to calculate continuously compounded interest.

    Parameters:
    P (float): the original principal sum
    r (float): the annual interest rate (as a decimal. For example, 5% = 0.05)
    t (float): the number of years the money is invested for

    Returns:
    float: total accumulation of principal including interest
    """
    # total accumulation of principal including interest = P*e^(rt)
    return P * math.exp(r * t)