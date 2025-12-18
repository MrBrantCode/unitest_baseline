"""
QUESTION:
Construct a query to retrieve the names, ages, and addresses of customers with the following conditions: age greater than 30, name starting with "J", and city in the address starting with "S".
"""

def get_customers_by_condition(customers):
    """
    Retrieves the names, ages, and addresses of customers with age greater than 30, 
    name starting with 'J', and city in the address starting with 'S'.

    Args:
        customers (list): A list of dictionaries where each dictionary represents a customer.

    Returns:
        list: A list of dictionaries containing the names, ages, and addresses of customers 
              that meet the specified conditions.
    """
    return [customer for customer in customers 
            if customer['age'] > 30 
            and customer['name'].startswith('J') 
            and customer['address'].startswith('S')]