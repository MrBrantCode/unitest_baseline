"""
QUESTION:
Calculate the additional amount the student needs to cover his accommodation and food expenses for the following year. The function should be named `calculate_additional_expenses`. The student's initial budget is $5000, the initial rent is $4000, the rent increase rate is 5%, the food expense increase rate is 3%, and the annual interest rate of the student's savings account is 2%.
"""

def calculate_additional_expenses(initial_budget, initial_rent, rent_increase_rate, food_expense_increase_rate, annual_interest_rate):
    """
    Calculate the additional amount the student needs to cover his accommodation and food expenses for the following year.

    Args:
        initial_budget (float): The student's initial budget.
        initial_rent (float): The initial rent.
        rent_increase_rate (float): The rent increase rate as a decimal.
        food_expense_increase_rate (float): The food expense increase rate as a decimal.
        annual_interest_rate (float): The annual interest rate of the student's savings account as a decimal.

    Returns:
        float: The additional amount the student needs to cover his accommodation and food expenses for the following year.
    """
    initial_food_expense = initial_budget - initial_rent
    new_rent = initial_rent + (initial_rent * rent_increase_rate)
    new_food_expense = initial_food_expense + (initial_food_expense * food_expense_increase_rate)
    new_total_cost = new_rent + new_food_expense
    savings = (initial_budget - initial_rent - initial_food_expense) * (1 + annual_interest_rate)
    additional_expenses = max(new_total_cost - initial_budget - savings, 0)
    return additional_expenses