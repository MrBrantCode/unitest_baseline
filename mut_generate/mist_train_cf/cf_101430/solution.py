"""
QUESTION:
Write a function `calculate_final_amount` that takes in the principal amount `P`, annual interest rate `r`, inflation rate `i`, compounding frequency `n`, and time period `t`, and returns the final amount after the given time period, considering compound interest with inflation. The interest is compounded `n` times per year for `t` years.
"""

def calculate_final_amount(P, r, i, n, t):
    """
    Calculate the final amount after the given time period, 
    considering compound interest with inflation.

    Args:
        P (float): The principal amount (initial investment)
        r (float): The annual interest rate (as a decimal)
        i (float): The inflation rate (as a decimal)
        n (int): The number of times the interest is compounded per year
        t (int): The number of years

    Returns:
        float: The final amount after the given time period
    """
    return P * (1 + (r - i)/n) ** (n*t)