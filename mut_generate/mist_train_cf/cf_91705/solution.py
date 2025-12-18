"""
QUESTION:
Write a function `compute_route_cost(distance_matrix, route)` to compute the cost of a route in a weighted graph. The function takes in a square weighted adjacency matrix `distance_matrix` and a list `route` representing the order of nodes visited. The function should return the total cost of the given route, which is the sum of the weights of the edges between consecutive nodes in the route.
"""

def compute_route_cost(distance_matrix, route):
    """
    Compute the cost of a route in a weighted graph.

    Args:
        distance_matrix (list of lists): A square weighted adjacency matrix.
        route (list): A list representing the order of nodes visited.

    Returns:
        int: The total cost of the given route.
    """
    total_cost = 0
    for i in range(len(route) - 1):
        source = route[i]
        destination = route[i + 1]
        total_cost += distance_matrix[source][destination]
    return total_cost