"""
QUESTION:
Implement the Nearest Neighbor function for the Traveling Salesman Problem. The function should take as input a 2D list representing the distances between nodes and return a list of node indices representing the order in which the nodes should be visited, starting and ending at node 0. The function should also return the total distance traveled.
"""

def traveling_salesman_problem(distances):
    """
    Solves the Traveling Salesman Problem using the Nearest Neighbor algorithm.

    Args:
        distances (list): A 2D list representing the distances between nodes.

    Returns:
        list: A list of node indices representing the order in which the nodes should be visited.
        int: The total distance traveled.
    """
    num_nodes = len(distances)
    visited = [False] * num_nodes
    visited[0] = True  # start at node 0
    path = [0]
    total_distance = 0

    for _ in range(num_nodes - 1):
        current_node = path[-1]
        next_node = None
        min_distance = float('inf')
        for i in range(num_nodes):
            if not visited[i] and distances[current_node][i] < min_distance:
                next_node = i
                min_distance = distances[current_node][i]
        visited[next_node] = True
        path.append(next_node)
        total_distance += min_distance

    # return to the starting node
    total_distance += distances[path[-1]][0]
    path.append(0)
    return path, total_distance