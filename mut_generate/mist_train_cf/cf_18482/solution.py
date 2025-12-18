"""
QUESTION:
Write a SQL query for a function named `get_recent_active_orders` that retrieves all records from the `Orders` table where the `status` is 'active', the `order_date` is within the last 30 days, and the `total_amount` is greater than $100.
"""

from datetime import datetime, timedelta

def get_recent_active_orders(orders):
    """
    Retrieves all records from the Orders table where the status is 'active', 
    the order_date is within the last 30 days, and the total_amount is greater than $100.

    Args:
        orders (list of dict): A list of dictionaries containing order information.

    Returns:
        list of dict: A list of active orders that meet the specified conditions.
    """
    thirty_days_ago = datetime.now() - timedelta(days=30)
    recent_active_orders = [order for order in orders 
                           if order['status'] == 'active' 
                           and order['order_date'] >= thirty_days_ago 
                           and order['total_amount'] > 100]
    return recent_active_orders