"""
QUESTION:
Write a SQL query to select the first name and last name of customers from the 'customers' table, excluding those with no orders, and sort the results in descending order of the number of orders each customer has made.
"""

def get_customers_with_orders(customers, orders):
    customer_orders = {}
    
    for order in orders:
        if order['customer_id'] not in customer_orders:
            customer_orders[order['customer_id']] = 1
        else:
            customer_orders[order['customer_id']] += 1
    
    customers_with_orders = []
    
    for customer in customers:
        if customer['customer_id'] in customer_orders and customer_orders[customer['customer_id']] > 0:
            customers_with_orders.append({
                'first_name': customer['first_name'],
                'last_name': customer['last_name'],
                'orders': customer_orders[customer['customer_id']]
            })
    
    return sorted(customers_with_orders, key=lambda x: x['orders'], reverse=True)