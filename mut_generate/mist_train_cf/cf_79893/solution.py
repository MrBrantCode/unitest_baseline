"""
QUESTION:
Implement a function called `a_star_search` to perform an A* search algorithm that uses a heuristic function to reduce the search space. The function should prioritize nodes based on the lowest combined cost and heuristic. The function should take as input a graph, a start node, a goal node, and a heuristic function, and return the shortest path from the start node to the goal node. The heuristic function should never overestimate the true cost to minimize the search space.
"""

import heapq

def a_star_search(graph, start, goal, heuristic):
    """
    Performs an A* search algorithm to find the shortest path from the start node to the goal node.
    
    Args:
    graph (dict): A dictionary representing the graph, where each key is a node and its corresponding value is a dictionary of its neighbors and their costs.
    start (node): The node to start the search from.
    goal (node): The node to search for.
    heuristic (function): A function that estimates the cost to reach the goal from a given node.
    
    Returns:
    list: The shortest path from the start node to the goal node.
    """
    
    # Initialize the OPEN list with the start node
    open_list = [(0, start)]
    
    # Initialize the CLOSED list as empty
    closed_list = set()
    
    # Initialize the cost and parent of each node
    cost = {start: 0}
    parent = {start: None}
    
    while open_list:
        # Look for the node with the lowest cost in the OPEN list
        current_cost, current_node = heapq.heappop(open_list)
        
        # If the current node is the goal, then stop and return the path
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1]
        
        # Add the current node to the CLOSED list
        closed_list.add(current_node)
        
        # Consider all adjacent nodes to the current node
        for neighbor, neighbor_cost in graph[current_node].items():
            # Calculate the new cost to the neighbor
            new_cost = cost[current_node] + neighbor_cost
            
            # If the neighbor is in the CLOSED list and the new cost is less than its assigned cost, update its parent and cost
            if neighbor in closed_list and new_cost < cost.get(neighbor, float('inf')):
                cost[neighbor] = new_cost
                parent[neighbor] = current_node
                heapq.heappush(open_list, (new_cost + heuristic(neighbor, goal), neighbor))
            # If the neighbor is not in both the OPEN list and the CLOSED list, calculate its cost and add it to the OPEN list
            elif neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = current_node
                heapq.heappush(open_list, (new_cost + heuristic(neighbor, goal), neighbor))
    
    # If there is no path to the goal, return failure
    return None