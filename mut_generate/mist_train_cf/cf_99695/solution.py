"""
QUESTION:
Create a function named `affordable_items` that takes two arguments: a list of budgets and a list of lists of prices. The function should return a dictionary where each key represents a budget and each value is a list of the affordable items corresponding to that budget, ignoring prices that exceed a budget.
"""

def affordable_items(budgets, price_lists):
    affordable_items_dict = {}
    for budget in budgets:
        affordable_items = []
        for price_list in price_lists:
            for price in price_list:
                if price <= budget:
                    affordable_items.append(price)
        affordable_items_dict[budget] = affordable_items
    return affordable_items_dict