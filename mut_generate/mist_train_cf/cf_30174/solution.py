"""
QUESTION:
Write a function `get_unique_orders` that takes a list of order IDs as input, where each ID can be either a string or an integer, and returns a new list containing only the unique order IDs in the same order as they appear in the input list. The function should not include duplicate order IDs in the output list, even if they appear multiple times in the input list.
"""

def get_unique_orders(order_id_list: list) -> list:
    unique_orders = []
    seen = set()
    for order_id in order_id_list:
        if order_id not in seen:
            unique_orders.append(order_id)
            seen.add(order_id)
    return unique_orders