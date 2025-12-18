"""
QUESTION:
Create a function called `total_orders` that takes two lists of order numbers as input: one for sales orders and one for sales shipments. The function should return the total number of distinct order numbers, considering that an order number may appear in either or both lists.
"""

def total_orders(sales_orders, sales_shipments):
    """
    Calculate the total number of distinct order numbers from sales orders and sales shipments.

    Args:
        sales_orders (list): A list of order numbers from sales orders.
        sales_shipments (list): A list of order numbers from sales shipments.

    Returns:
        int: The total number of distinct order numbers.
    """
    # Combine the two lists and convert to a set to eliminate duplicates
    combined_orders = set(sales_orders + sales_shipments)
    
    # Return the total number of distinct order numbers
    return len(combined_orders)