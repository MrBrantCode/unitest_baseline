"""
QUESTION:
Implement the `aStar` function to find the shortest path in a weighted graph from the start node to the goal node using the A* algorithm. The graph is represented as an adjacency list and each edge has an associated non-negative cost. The function should take the graph, start node, and goal node as input and return the shortest path as a list of nodes from the start node to the goal node.
"""

import heapq

def aStar(graph, start, goal, heuristic_estimate):
    open_set = [(0, start, [])]  # (estimated_total_cost, current_node, path)
    closed_set = set()

    while open_set:
        estimated_total_cost, current_node, path = heapq.heappop(open_set)
        if current_node == goal:
            return path + [current_node]

        if current_node in closed_set:
            continue

        closed_set.add(current_node)

        for neighbor, cost in graph.get(current_node, []):
            if neighbor in closed_set:
                continue
            new_path = path + [current_node]
            estimated_cost_to_neighbor = len(new_path) + cost + heuristic_estimate(neighbor, goal)
            heapq.heappush(open_set, (estimated_cost_to_neighbor, neighbor, new_path))

    return None  # No path found