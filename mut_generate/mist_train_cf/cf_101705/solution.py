"""
QUESTION:
Write a Python function named `calculate_compound_interest` that takes the principal amount `P`, annual interest rate `r` (as a decimal), inflation rate `i` (as a decimal), number of times the interest is compounded per year `n`, and the number of years `t` as parameters. The function should return the final amount `A` after `t` years using the compound interest formula with inflation.
"""

def calculate_compound_interest(P, r, i, n, t):
    """
    Calculate the final amount after t years using the compound interest formula with inflation.

    Args:
        P (float): The principal amount (initial investment)
        r (float): The annual interest rate (as a decimal)
        i (float): The inflation rate (as a decimal)
        n (int): The number of times the interest is compounded per year
        t (int): The number of years

    Returns:
        float: The final amount A after t years
    """
    return P * (1 + (r - i) / n) ** (n * t)