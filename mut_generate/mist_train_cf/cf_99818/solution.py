"""
QUESTION:
Create a function called `calculate_profit` that takes four parameters: `total_revenue`, `cost_of_goods_sold`, `operating_expenses`, and `taxes`. Using the formula `profit = total_revenue - cost_of_goods_sold - operating_expenses - taxes`, calculate and return the total profit. Assume all input values are numeric and will be provided in the same currency.
"""

def calculate_profit(total_revenue, cost_of_goods_sold, operating_expenses, taxes):
    """
    Calculate the total profit using the formula:
    profit = total_revenue - cost_of_goods_sold - operating_expenses - taxes

    Args:
        total_revenue (float): Total amount of money earned from sales.
        cost_of_goods_sold (float): Total cost of producing or purchasing the goods sold.
        operating_expenses (float): Costs incurred in running the business.
        taxes (float): Taxes owed on the profits earned.

    Returns:
        float: The total profit.
    """
    return total_revenue - cost_of_goods_sold - operating_expenses - taxes