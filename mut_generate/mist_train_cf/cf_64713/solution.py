"""
QUESTION:
Create a function `calculate_travel_route` that takes as input a list of routes between two points, where each route is represented as a dictionary with 'cost' and 'time' keys. The function should also take two weights, `cost_weight` and `time_weight`, representing the relative importance of cost and time. The function should return the route with the best score, calculated as `(cost_weight * cost) + (time_weight * time)`.
"""

def calculate_travel_route(routes, cost_weight, time_weight):
    """
    Calculate the best travel route based on cost and time.

    Args:
    routes (list): A list of dictionaries, each containing 'cost' and 'time' keys.
    cost_weight (float): The relative importance of cost.
    time_weight (float): The relative importance of time.

    Returns:
    dict: The route with the best score.
    """
    best_route = min(routes, key=lambda route: (cost_weight * route['cost']) + (time_weight * route['time']))
    return best_route