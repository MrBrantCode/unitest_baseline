"""
QUESTION:
Write a Python function named `calculate_profit` that takes four parameters: `total_revenue`, `cost_of_goods_sold`, `operating_expenses`, and `taxes`. The function should return the total profit calculated by subtracting `cost_of_goods_sold`, `operating_expenses`, and `taxes` from `total_revenue`.
"""

def calculate_profit(total_revenue, cost_of_goods_sold, operating_expenses, taxes):
    """
    Calculate the total profit by subtracting cost_of_goods_sold, operating_expenses, and taxes from total_revenue.
    
    Parameters:
    total_revenue (float): The total amount of money earned from sales.
    cost_of_goods_sold (float): The total cost of producing or purchasing the goods sold.
    operating_expenses (float): The costs incurred in running the business.
    taxes (float): Any taxes owed on the profits earned.
    
    Returns:
    float: The total profit.
    """
    return total_revenue - cost_of_goods_sold - operating_expenses - taxes