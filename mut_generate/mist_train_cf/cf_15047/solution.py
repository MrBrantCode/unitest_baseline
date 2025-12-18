"""
QUESTION:
Calculate the function `compound_interest(principal, interest_rate, time, n)` that returns a list of the total amount of money at the end of each year, and the total amount after the specified time period. 

The function takes four parameters: 
- `principal`: the initial amount of money invested (in dollars)
- `interest_rate`: the annual interest rate (as a decimal)
- `time`: the number of years the money is invested for
- `n`: the number of times that interest is compounded per year

Use the compound interest formula A = P(1 + r/n)^(nt) to calculate the future value of the investment for each year.
"""

def compound_interest(principal, interest_rate, time, n):
    """
    Calculate the total amount of money at the end of each year and 
    the total amount after the specified time period using compound interest formula.

    Args:
        principal (float): The initial amount of money invested (in dollars)
        interest_rate (float): The annual interest rate (as a decimal)
        time (int): The number of years the money is invested for
        n (int): The number of times that interest is compounded per year

    Returns:
        list: A list containing the total amount at the end of each year and 
              the total amount after the specified time period
    """
    total_amounts = []
    for year in range(1, time + 1):
        amount = principal * (1 + interest_rate / n) ** (n * year)
        total_amounts.append(amount)
    return total_amounts