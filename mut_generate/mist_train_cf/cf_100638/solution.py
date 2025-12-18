"""
QUESTION:
Write a Python function named `customer_order` that takes in a customer name and an optional parameter `sort_order` to retrieve and return the order numbers associated with the given customer name from a dictionary. The function should use a binary search algorithm for searching within the list of order numbers, and the `sort_order` parameter should allow for sorting the order numbers in descending order before returning them. The function should return an empty list if the customer name is not found in the dictionary.
"""

def customer_order(customer_name, sort_order=None):
    table = {'Alice': [100, 200, 300], 'Bob': [150, 250], 'Charlie': [175, 225, 350]}
    if customer_name in table:
        order_numbers = table[customer_name]
        if sort_order == 'descending':
            order_numbers.sort(reverse=True)
        return order_numbers
    else:
        return []