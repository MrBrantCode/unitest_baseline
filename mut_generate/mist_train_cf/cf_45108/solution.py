"""
QUESTION:
Determine the allocation of funds between two investments with annual interest yields of 6% and 8%, given an initial investment amount of $1000 and a total cumulative income of $75 after one year. Write a function called `allocate_investments` to solve for the amounts invested at each rate.
"""

def allocate_investments(initial_investment, total_income, rate1, rate2):
    """
    Determine the allocation of funds between two investments with annual interest yields.

    Args:
        initial_investment (float): The initial investment amount.
        total_income (float): The total cumulative income after one year.
        rate1 (float): The first annual interest rate.
        rate2 (float): The second annual interest rate.

    Returns:
        tuple: A tuple containing the amounts invested at each rate.
    """

    # Calculate the amount invested at the first rate
    investment_at_rate1 = (total_income - (initial_investment * rate2)) / (rate1 - rate2)

    # Calculate the amount invested at the second rate
    investment_at_rate2 = initial_investment - investment_at_rate1

    return investment_at_rate1, investment_at_rate2