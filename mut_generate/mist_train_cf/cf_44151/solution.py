"""
QUESTION:
Write a function `A_star` that implements the A* search algorithm with a heuristic to find the shortest path from a start node to a goal node in a graph. The function should take as input a graph, a start node, and a goal node, and return the shortest path from the start node to the goal node. The function should use a priority queue to explore nodes in order of their estimated total cost (the cost of the path from the start node to the current node plus the estimated cost from the current node to the goal node), and should handle conflicts between nodes with the same estimated cost by prioritizing the most recently encountered node. The function should also handle exceptions where the queue is empty or there is no path to the goal node.
"""

def A_star(graph, start_node, goal):
    """
    This function implements the A* search algorithm with a heuristic to find the shortest path 
    from a start node to a goal node in a graph.

    Args:
        graph: A graph represented as a dictionary where each key is a node and its value is 
               another dictionary with its neighbors and their costs.
        start_node: The node to start the search from.
        goal: The goal node to search for.

    Returns:
        A list of nodes representing the shortest path from the start node to the goal node.

    Raises:
        Exception: If the queue is empty or there is no path to the goal node.
    """

    # Initialize costs and previous nodes
    for node in graph:
        graph[node]['cost'] = float('inf')
        graph[node]['prev'] = None
    graph[start_node]['cost'] = 0

    # Define the heuristic function (Manhattan distance)
    def heuristic(node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    # Define the priority queue
    queue = []
    def add(node):
        queue.append((graph[node]['cost'] + heuristic(node, goal), node))
    def pop():
        if not queue:
            raise Exception("Queue is empty")
        queue.sort()
        return queue.pop(0)[1]

    # Add the start node to the queue
    add(start_node)

    while queue:
        current_node = pop()
        if current_node == goal:
            # Reconstruct the path
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = graph[current_node]['prev']
            return path[::-1]

        for neighbor, cost in graph[current_node]['neighbors'].items():
            tentative_cost = graph[current_node]['cost'] + cost
            if tentative_cost < graph[neighbor]['cost']:
                graph[neighbor]['cost'] = tentative_cost
                graph[neighbor]['prev'] = current_node
                add(neighbor)

    raise Exception("No path to goal")