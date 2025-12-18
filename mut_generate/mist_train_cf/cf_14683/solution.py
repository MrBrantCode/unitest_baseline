"""
QUESTION:
Implement a function called `sort_customers` that takes a list of customer information and a sorting attribute as input, and returns the sorted list. The customer information is represented as a dictionary with keys 'name', 'registration_date', and 'total_purchase_amount', and the sorting attribute can be 'name', 'registration_date', or 'total_purchase_amount'. The function should also handle cases where the sorting attribute is not one of the specified options.

Additionally, implement a function called `filter_customers` that takes a list of customer information and a list of filters as input, and returns the filtered list. The filters are represented as strings in the format 'key:value', where 'key' can be 'age', 'location', or 'order_history'. The function should filter the customers based on the specified criteria.

Both functions should be implemented in a way that allows them to be used in a REST API to retrieve and sort customer information.
"""

def sort_customers(customers, sort_by):
    """
    Sorts the list of customers based on the specified attribute.

    Args:
    customers (list): A list of customer dictionaries.
    sort_by (str): The attribute to sort by. Can be 'name', 'registration_date', or 'total_purchase_amount'.

    Returns:
    list: The sorted list of customers.
    """
    if sort_by == 'name':
        return sorted(customers, key=lambda customer: customer['name'])
    elif sort_by == 'registration_date':
        return sorted(customers, key=lambda customer: customer['registration_date'])
    elif sort_by == 'total_purchase_amount':
        return sorted(customers, key=lambda customer: customer['total_purchase_amount'])
    else:
        return customers


def filter_customers(customers, filters):
    """
    Filters the list of customers based on the specified criteria.

    Args:
    customers (list): A list of customer dictionaries.
    filters (list): A list of filters in the format 'key:value'.

    Returns:
    list: The filtered list of customers.
    """
    filtered_customers = customers

    for filter in filters:
        key, value = filter.split(':')
        if key == 'age':
            filtered_customers = [customer for customer in filtered_customers if customer['age'] == int(value)]
        elif key == 'location':
            filtered_customers = [customer for customer in filtered_customers if customer['location'] == value]
        elif key == 'order_history':
            filtered_customers = [customer for customer in filtered_customers if value in customer['order_history']]

    return filtered_customers