"""
QUESTION:
Create a function `customer_order(customer_name, sort_order=None)` that takes a customer name and an optional `sort_order` parameter as input. The function should return a list of order numbers for the given customer name from a predefined dictionary. If `sort_order` is 'descending', the function should sort the order numbers in descending order before returning them.
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