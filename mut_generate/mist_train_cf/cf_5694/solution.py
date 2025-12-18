"""
QUESTION:
Write a SQL query named `last_three_orders` that retrieves the last three records from the "Orders" table, excluding records with a total value less than or equal to 15. The query should also join the "Customers" table to retrieve the customer's name, email, and address, but only for customers whose name starts with the letter "J". The query should be optimized for performance and avoid subqueries.
"""

def last_three_orders(orders, customers):
    # Filter the customers whose name starts with 'J'
    filtered_customers = [c for c in customers if c['name'].startswith('J')]

    # Join the customers with the orders
    joined_data = [(c, o) for c in filtered_customers for o in orders if c['customer_id'] == o['customer_id'] and o['total'] > 15]

    # Sort the data by order date and retrieve the last three records
    sorted_data = sorted(joined_data, key=lambda x: x[1]['order_date'], reverse=True)[:3]

    # Return the required information
    return [(c['name'], c['email'], c['address']) for c, o in sorted_data]