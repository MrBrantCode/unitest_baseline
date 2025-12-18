"""
QUESTION:
Function Name: cost

Information: Given a list of places (nodes) and the costs of traveling between them (edges), determine the optimal travel route with the minimum total cost. The cost of traveling from one point to another is provided by the function cost(s, d).

Restriction: The function should return the optimal travel route with the minimum total cost, considering all possible routes and their corresponding costs.
"""

def cost(s, d, graph):
    """
    Returns the cost of traveling from point s to point d.

    Args:
    s (str): Starting point.
    d (str): Destination point.
    graph (dict): Dictionary representing the graph where keys are node pairs and values are costs.

    Returns:
    int: Cost of traveling from s to d.
    """
    return graph.get((s, d), float('inf'))  # Return infinity if no direct edge exists


def entrance(graph, start_node):
    """
    Finds the optimal travel route with the minimum total cost.

    Args:
    graph (dict): Dictionary representing the graph where keys are node pairs and values are costs.
    start_node (str): Starting node.

    Returns:
    int: Minimum total cost.
    """
    visited_nodes = [start_node]
    total_cost = 0
    current_node = start_node

    while len(visited_nodes) < len(graph):
        min_cost = float('inf')
        next_node = None

        for node in graph:
            if node[0] == current_node and node[1] not in visited_nodes:
                edge_cost = graph[node]
                if edge_cost < min_cost:
                    min_cost = edge_cost
                    next_node = node[1]

        if next_node is None:
            break

        total_cost += min_cost
        visited_nodes.append(next_node)
        current_node = next_node

    # Add cost to return to the start node
    total_cost += cost(current_node, start_node, graph)

    return total_cost