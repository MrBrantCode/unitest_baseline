"""
QUESTION:
Create a function named `affordable_items` that takes two arguments, `budgets` and `price_lists`, where `budgets` is a list of budgets and `price_lists` is a list of lists of prices. The function should return a dictionary where each key represents a budget, and each value is a list of the affordable items (prices) corresponding to that budget. If a price exceeds a budget, it should be ignored.
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