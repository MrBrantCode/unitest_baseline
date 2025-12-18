"""
QUESTION:
Write a function `compound_interest_with_inflation` that calculates the final amount after a specified number of years, given the principal amount, annual interest rate, inflation rate, and the number of times the interest is compounded per year. The function should take four parameters: `P` (the principal amount), `r` (the annual interest rate as a decimal), `i` (the inflation rate as a decimal), and `n` (the number of times the interest is compounded per year), and `t` (the number of years). The function should return the final amount after `t` years.
"""

def compound_interest_with_inflation(P, r, i, n, t):
    """
    Calculates the final amount after a specified number of years, 
    given the principal amount, annual interest rate, inflation rate, 
    and the number of times the interest is compounded per year.

    Args:
    P (float): The principal amount.
    r (float): The annual interest rate as a decimal.
    i (float): The inflation rate as a decimal.
    n (int): The number of times the interest is compounded per year.
    t (int): The number of years.

    Returns:
    float: The final amount after t years.
    """
    return P * (1 + (r - i)/n) ** (n*t)