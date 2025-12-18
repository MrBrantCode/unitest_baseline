"""
QUESTION:
Write a function named `dijkstras` that takes as input a graph represented as a dictionary of adjacency lists and a start node, and returns a dictionary of the shortest distances from the start node to all other nodes in the graph. The function should use Dijkstra's algorithm to find the shortest distances. 

The input graph is represented as a dictionary where each key is a node and its corresponding value is another dictionary. The inner dictionary's keys are the node's neighbors and its values are the edge weights. 

The function should handle graphs that do not have negative edges. It should also be efficient for finding the shortest paths from a source node to all other nodes in the graph.

Note that the function should be able to handle real-world complications such as a graph's size and complexity.
"""

def dijkstras(graph, start_node):
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start_node] = 0
    unvisited_nodes = list(graph.keys())

    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda node: shortest_distances[node])
        unvisited_nodes.remove(current_node)
        
        for neighbour, distance in graph[current_node].items():
            if neighbour not in unvisited_nodes:
                continue
            new_distance = shortest_distances[current_node] + distance
            if new_distance < shortest_distances[neighbour]:
                shortest_distances[neighbour] = new_distance

    return shortest_distances