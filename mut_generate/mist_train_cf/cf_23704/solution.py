"""
QUESTION:
Write a function `depthFirstSearch` that performs a depth-first search on a graph. The function should take two parameters: `graph` and `start_node`, where `graph` is a dictionary representing the graph with nodes as keys and a list of adjacent nodes as values, and `start_node` is the node where the search begins. The function should return a set of visited nodes.
"""

def depthFirstSearch(graph, start_node):
    """
    Performs a depth-first search on a graph.

    Args:
    graph (dict): A dictionary representing the graph with nodes as keys and a list of adjacent nodes as values.
    start_node: The node where the search begins.

    Returns:
    set: A set of visited nodes.
    """
    visited = set()
    def dfs(node):
        # Add the current node to the visited set
        visited.add(node)
        # Iterate over the adjacent nodes of the current node
        for adjacent_node in graph.get(node, []):
            # If the adjacent node has not been visited, recursively visit it
            if adjacent_node not in visited:
                dfs(adjacent_node)
    # Start the depth-first search at the start node
    dfs(start_node)
    return visited