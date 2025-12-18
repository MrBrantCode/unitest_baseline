"""
QUESTION:
Write a function named `fruit_distribution` that takes four parameters: `s`, a list of strings representing the quantity of various fruits, `n`, the total value of fruits, `fruits`, a list of all fruit types, and `fruit_prices`, a dictionary containing the prices of each fruit. Return a dictionary illustrating the quantity of each fruit absent from the list, calculated using price and overall cost. The output dictionary should only include fruits with a count not equal to zero.
"""

def fruit_distribution(s, n, fruits, fruit_prices):
    # Initialize fruit quantities
    stock = {fruit: 0 for fruit in fruits}
    # Update quantities from inventory
    for fruit_info in s:
        quantity, fruit = fruit_info.split(" ")
        stock[fruit] = int(quantity)
    # Calculate current worth of the inventory
    worth = sum(stock[fruit] * fruit_prices[fruit] for fruit in fruits)
    # Calculate remaining worth and distribute among fruits not in list
    remaining_worth = n - worth
    return {fruit: remaining_worth // fruit_prices[fruit] for fruit in fruits if stock[fruit]==0 and fruit_prices[fruit]<=remaining_worth}