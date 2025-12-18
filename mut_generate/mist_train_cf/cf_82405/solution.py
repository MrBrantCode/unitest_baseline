"""
QUESTION:
Create a function `calculate_budget(salary, budget_splits)` that calculates the amount spent on each category, the expenses on "Others", and savings. The function takes two arguments: an integer `salary` representing the monthly salary and a dictionary `budget_splits` where keys are the budget categories (strings) and values are the respective percentages (floats from 0 to 1). The function should return a dictionary with the same keys as `budget_splits` along with two additional keys, "others" and "savings". If the sum of percentages in `budget_splits` surpasses 100%, the function should return an error message.
"""

def calculate_budget(salary, budget_splits):
    # Check if sum of percentages in budget_splits is more than 100%
    if sum(budget_splits.values()) > 1:
        return 'Error: The sum of percentages in budget_splits cannot be more than 100%'

    # Calculate the expenses for each category
    budget_splits_amt = {k: v * salary for k, v in budget_splits.items()}

    # Calculate the total expenses and savings
    total_expenses_no_others = sum(budget_splits_amt.values())
    others = 0.0  # Initialize "Others" category
    savings = salary - total_expenses_no_others - others  # Calculate savings

    # If calculated savings is negative, some of the negative amount should belong to "Others"
    if savings < 0:
        others -= savings  # Add the negative savings to "Others"
        savings = 0.0  # Reset savings to zero

    # Add the "Others" and "savings" keys to the dictionary
    budget_splits_amt["others"] = others
    budget_splits_amt["savings"] = savings

    return budget_splits_amt