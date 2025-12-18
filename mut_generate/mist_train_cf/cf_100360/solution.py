"""
QUESTION:
Create a function named `rectify_expenses` that takes a list of expenses and two optional parameters: `category` and `category_name`. The `category` parameter should default to `None` and `category_name` should default to `"transportation"`. The function should return a dictionary with two keys: `total_transportation` and `total_expenses`. The function should sum the amounts of all expenses that match the specified category or category name and assign this sum to `total_transportation`. The function should also sum the amounts of all expenses that do not match the specified category or category name and assign this sum to `total_expenses`. If there are multiple expenses with the same category name, the function should handle this correctly by summing the amounts of all matching expenses.
"""

def rectify_expenses(expenses, category=None, category_name="transportation"):
    total_transportation = 0
    total_expenses = 0
    
    if category is None:
        total_transportation = sum(expense['amount'] for expense in expenses if expense['category'] == category_name)
        total_expenses = sum(expense['amount'] for expense in expenses if expense['category'] != category_name)
    else:
        total_transportation = sum(expense['amount'] for expense in expenses if expense['category'] == category)
        total_expenses = sum(expense['amount'] for expense in expenses if expense['category'] != category)

    rectified_expenses = {
        'total_transportation': total_transportation,
        'total_expenses': total_expenses
    }
    
    return rectified_expenses