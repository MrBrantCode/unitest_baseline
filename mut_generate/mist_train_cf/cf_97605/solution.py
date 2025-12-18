"""
QUESTION:
Create a function `calculate_compound_interest` that takes five parameters: the principal amount (`P`), annual interest rate (`r`), inflation rate (`i`), number of times interest is compounded per year (`n`), and number of years (`t`). The function should return the final amount after `t` years, considering the compound interest with inflation.
"""

def calculate_compound_interest(P, r, i, n, t):
    """
    Calculate the final amount after t years, considering the compound interest with inflation.

    Args:
        P (float): The principal amount (initial investment)
        r (float): The annual interest rate (as a decimal)
        i (float): The inflation rate (as a decimal)
        n (int): The number of times the interest is compounded per year
        t (int): The number of years

    Returns:
        float: The final amount after t years
    """
    return P * (1 + (r - i)/n) ** (n*t)