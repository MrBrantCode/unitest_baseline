"""
QUESTION:
Write a function named `get_customers_with_high_value_orders` that retrieves customer IDs and names where the customer ID starts with 'C' and they have ordered at least two distinct products priced over $100 each. The results should be sorted in descending order of the total price of their orders.
"""

def get_customers_with_high_value_orders(customers, orders, order_products, products):
    """
    Retrieves customer IDs and names where the customer ID starts with 'C' and 
    they have ordered at least two distinct products priced over $100 each.

    Args:
    customers (list): A list of dictionaries containing customer information.
    orders (list): A list of dictionaries containing order information.
    order_products (list): A list of dictionaries containing order-product information.
    products (list): A list of dictionaries containing product information.

    Returns:
    list: A list of dictionaries containing customer IDs and names, sorted by total price in descending order.
    """
    # Initialize an empty dictionary to store the results
    result = {}

    # Iterate over each customer
    for customer in customers:
        if customer['customer_id'].startswith('C'):
            # Initialize variables to track total price and distinct products
            total_price = 0
            distinct_products = set()

            # Iterate over each order
            for order in orders:
                if order['customer_id'] == customer['customer_id']:
                    # Iterate over each order-product
                    for order_product in order_products:
                        if order_product['order_id'] == order['order_id']:
                            # Iterate over each product
                            for product in products:
                                if product['product_id'] == order_product['product_id']:
                                    # Check if the product price is over $100
                                    if product['price'] > 100:
                                        # Add the product price to the total price
                                        total_price += product['price']
                                        # Add the product ID to the set of distinct products
                                        distinct_products.add(product['product_id'])

            # Check if the customer has ordered at least two distinct products
            if len(distinct_products) >= 2:
                # Add the customer to the result dictionary
                result[customer['customer_id']] = {
                    'customer_name': customer['customer_name'],
                    'total_price': total_price
                }

    # Sort the result dictionary by total price in descending order
    sorted_result = sorted(result.values(), key=lambda x: x['total_price'], reverse=True)

    return sorted_result