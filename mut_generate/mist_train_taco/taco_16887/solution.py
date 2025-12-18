"""
QUESTION:
You love coffee and want to know what beans you can afford to buy it.

The first argument to your search function will be a number which represents your budget.

The second argument will be an array of coffee bean prices.

Your 'search' function should return the stores that sell coffee within your budget. 

The search function should return a string of prices for the coffees beans you can afford. The prices in this string are to be sorted in ascending order.
"""

def find_affordable_coffee_beans(budget, prices):
    """
    Finds and returns the prices of coffee beans that are within the given budget.

    Parameters:
    - budget (int or float): The maximum amount of money you can spend.
    - prices (list of int or float): A list of prices for the coffee beans available at different stores.

    Returns:
    - str: A string containing the prices of coffee beans that are within the budget, sorted in ascending order, and separated by commas.
    """
    return ','.join((str(price) for price in sorted(prices) if price <= budget))