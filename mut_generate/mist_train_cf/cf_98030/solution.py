"""
QUESTION:
Create a function called `rectify_expenses` that takes a list of expenses and two optional parameters: `category` and `category_name`. The function should return a dictionary containing the total amount of expenses in the specified category and the total amount of all other expenses. If `category` is not `None`, the function should remove all expenses with the specified category. Otherwise, it should remove all expenses with the category name specified in `category_name`, defaulting to "transportation" if not specified. The function should handle multiple expenses with the same category name.
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