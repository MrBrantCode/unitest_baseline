"""
QUESTION:
Write a function named `find_customers` that takes no arguments and returns all records from the customers table. The function should filter records based on the following criteria: the state is "California", the phone number starts with "555", the last name starts with "S", and the first name starts with either "A" or "B".
"""

def find_customers(customers):
    """
    Filter customer records based on specific criteria.

    Args:
        customers (list): A list of customer records.
            Each record is a dictionary containing 'state', 'phone_number', 'last_name', and 'first_name'.

    Returns:
        list: A list of filtered customer records.
    """
    return [customer for customer in customers 
            if customer['state'] == 'California' 
            and customer['phone_number'].startswith('555') 
            and customer['last_name'].startswith('S') 
            and (customer['first_name'].startswith('A') or customer['first_name'].startswith('B'))]