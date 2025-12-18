"""
QUESTION:
Write a function to select customers with a name starting with 'A' and a phone number ending with '9'. The function should return a list of customers matching the given criteria.

Function name: select_customers
Input: customers table with columns 'name' and 'phone_number'
Output: A list of customers with 'name' starting with 'A' and 'phone_number' ending with '9'
"""

def select_customers(customers):
    """
    Select customers with a name starting with 'A' and a phone number ending with '9'.

    Args:
        customers (list of dictionaries): A list of dictionaries containing 'name' and 'phone_number' keys.

    Returns:
        list of dictionaries: A list of customers matching the given criteria.
    """
    return [customer for customer in customers if customer['name'].startswith('A') and customer['phone_number'].endswith('9')]