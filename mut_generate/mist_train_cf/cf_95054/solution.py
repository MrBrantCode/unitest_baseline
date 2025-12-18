"""
QUESTION:
Write a function named `compute_route_cost` that calculates the total cost of a route in a weighted graph. 

The function should take in three parameters: a square weighted adjacency matrix `distance_matrix` where the value at index `i, j` represents the weight of the edge between node `i` and node `j`, a list `route` representing the order of visited nodes, and an integer `start_node` representing the starting node of the route. 

The function should return the total cost of the route, which is the sum of the weights of the edges between consecutive nodes in the route.
"""

def compute_route_cost(distance_matrix, route, start_node):
    total_cost = 0
    
    current_node = start_node
    
    for next_node in route:
        total_cost += distance_matrix[current_node][next_node]
        current_node = next_node
    
    return total_cost