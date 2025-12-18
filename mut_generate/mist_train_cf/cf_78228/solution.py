"""
QUESTION:
Write a function `calculate_total_cost` that takes the initial number of stamps, initial cost, and the goal number of stamps as parameters, and returns the total cost to acquire the goal number of stamps at the same spending rate. The function should round the result to two decimal places.
"""

def calculate_total_cost(initial_stamps, initial_cost, goal_stamps):
    """
    Calculate the total cost to acquire the goal number of stamps at the same spending rate.

    Args:
        initial_stamps (int): The initial number of stamps.
        initial_cost (float): The initial cost.
        goal_stamps (int): The goal number of stamps.

    Returns:
        float: The total cost to acquire the goal number of stamps, rounded to two decimal places.
    """
    cost_per_stamp = initial_cost / initial_stamps
    total_cost = goal_stamps * cost_per_stamp
    return round(total_cost, 2)