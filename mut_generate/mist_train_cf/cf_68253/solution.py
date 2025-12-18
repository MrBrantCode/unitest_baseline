"""
QUESTION:
Create a function named `optimized_order_route` that takes two lists, `orders` and `distances`, of the same length as input and returns a list of orders in the optimized route. The optimized route is determined by sorting the orders based on their corresponding distances in ascending order. The function should not consider any real-life constraints or intricacies of route planning.
"""

def optimized_order_route(orders, distances):
    """
    Returns a list of orders in the optimized route.
    
    The optimized route is determined by sorting the orders based on their corresponding distances in ascending order.

    Parameters:
    orders (list): A list of orders.
    distances (list): A list of distances corresponding to the orders.

    Returns:
    list: A list of orders in the optimized route.
    """
    # Create a list of tuples, each tuple representing an order with its corresponding distance
    order_distance_pairs = list(zip(orders, distances))

    # Sort the list of tuples based on the distance
    order_distance_pairs.sort(key=lambda x: x[1])

    # Return optimized order route
    return [order for order, _ in order_distance_pairs]