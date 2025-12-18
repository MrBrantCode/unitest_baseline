"""
QUESTION:
Write a function `rectify_expenses` that takes in a list of expenses, a transportation amount, and an optional transportation name. The function should remove any expenses with the given transportation name from the list, calculate the total expenses without the transportation costs, and append a new transportation expense with the given amount and name. It should also append the total expense to the end of the list. If multiple transportation expenses exist, the function should handle them correctly. The default transportation name should be "Transportation".
"""

def rectify_expenses(expenses, transportation_amount, transportation_name="Transportation"):
    transportation_expenses = [int(expense.split(":")[-1]) for expense in expenses if transportation_name in expense]
    for expense in transportation_expenses:
        expenses.remove(f"{transportation_name}:{expense}")
    
    total_expense = sum([int(expense.split(":")[-1]) for expense in expenses])
    
    expenses.append(f"{transportation_name}:{transportation_amount}")
    expenses.append(f"Total:{total_expense + transportation_amount}")
    return expenses