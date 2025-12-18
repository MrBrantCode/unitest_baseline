"""
QUESTION:
Create a function named `calculate_route_cost` that takes a 2D list `distance_matrix` and a list of integers `route` as input, and returns the total cost of the route. The cost is calculated by summing the distances between consecutive points in the route, where the distance between two points is given by the corresponding value in the `distance_matrix`. The function should assume that the `distance_matrix` is a square matrix and that the `route` list contains valid indices for the matrix.
"""

def calculate_route_cost(distance_matrix, route):
    cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
    return cost