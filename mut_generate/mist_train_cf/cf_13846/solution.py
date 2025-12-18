"""
QUESTION:
Write a SQL query to retrieve all customers whose customer ID starts with "C" and have at least two distinct products in their orders with a price greater than $100. The query should return customer_id and customer_name.
"""

def customer_with_expensive_orders(customers, orders, order_details, products):
    result = []
    for customer in customers:
        if not customer['customer_id'].startswith('C'):
            continue
        customer_orders = [order for order in orders if order['customer_id'] == customer['customer_id']]
        expensive_product_ids = set()
        for order in customer_orders:
            for order_detail in order_details:
                if order_detail['order_id'] == order['order_id']:
                    for product in products:
                        if product['product_id'] == order_detail['product_id'] and product['price'] > 100:
                            expensive_product_ids.add(product['product_id'])
        if len(expensive_product_ids) >= 2:
            result.append({'customer_id': customer['customer_id'], 'customer_name': customer['customer_name']})
    return result