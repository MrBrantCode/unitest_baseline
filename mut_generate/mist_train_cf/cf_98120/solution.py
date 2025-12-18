"""
QUESTION:
Create a function `group_orders` that groups similar product orders together based on customer purchase history and order details. 

The function takes a list of orders as input, where each order is a dictionary containing `id`, `customer_id`, `order_date`, and `product`. The function should return a dictionary where the keys are the customer IDs and the values are lists of orders associated with each customer ID. The orders in each list should be merged if they have the same product, and the order with the smallest ID should be kept.
"""

def group_orders(orders):
    """
    Groups similar product orders together based on customer purchase history and order details.

    Args:
    orders (list): A list of orders where each order is a dictionary containing 'id', 'customer_id', 'order_date', and 'product'.

    Returns:
    dict: A dictionary where the keys are the customer IDs and the values are lists of orders associated with each customer ID.
    """
    grouped_orders = {}
    for order in sorted(orders, key=lambda x: (x["customer_id"], x["order_date"])):
        customer_id = order["customer_id"]
        product = order["product"]

        if customer_id not in grouped_orders:
            grouped_orders[customer_id] = [order]
        else:
            for other_order in grouped_orders[customer_id]:
                if other_order["product"] == product:
                    other_order["id"] = min(other_order["id"], order["id"])
                    break
            else:
                grouped_orders[customer_id].append(order)

        for other_customer_id, other_orders in grouped_orders.items():
            if other_customer_id != customer_id:
                for other_order in other_orders:
                    if other_order["product"] == product:
                        other_order["id"] = min(other_order["id"], order["id"])
                        grouped_orders[customer_id].extend(
                            [o for o in other_orders if o["product"] == product and o["id"] != other_order["id"]]
                        )
                        grouped_orders[other_customer_id] = [
                            o for o in other_orders if o["product"] != product or o["id"] == other_order["id"]
                        ]
    return grouped_orders