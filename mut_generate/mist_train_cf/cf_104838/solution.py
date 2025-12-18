"""
QUESTION:
Write a function `get_high_value_customers` that retrieves the names of customers who have placed at least 5 orders and have spent a total of $1000 or more on their orders. The function does not need to take any arguments.
"""

def get_high_value_customers(orders):
    """
    Retrieves the names of customers who have placed at least 5 orders and have spent a total of $1000 or more on their orders.

    Args:
    orders (list): A list of dictionaries where each dictionary contains information about a customer's order.
                   Each dictionary should have the keys 'customer_name', 'order_id', and 'order_total'.

    Returns:
    list: A list of customer names who meet the specified criteria.
    """
    customer_orders = {}
    
    # Group orders by customer
    for order in orders:
        customer_name = order['customer_name']
        if customer_name not in customer_orders:
            customer_orders[customer_name] = {'count': 0, 'total': 0.0}
        
        customer_orders[customer_name]['count'] += 1
        customer_orders[customer_name]['total'] += order['order_total']
    
    # Filter customers who have placed at least 5 orders and have spent a total of $1000 or more
    high_value_customers = [name for name, order_info in customer_orders.items() 
                           if order_info['count'] >= 5 and order_info['total'] >= 1000]
    
    return high_value_customers