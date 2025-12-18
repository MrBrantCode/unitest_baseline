"""
QUESTION:
Implement the Bellman-Ford function to find the shortest path from a source vertex to all other vertices in a weighted graph. The graph is represented as a list of edges, where each edge is represented as a tuple (u, v, w) where u is the source vertex, v is the destination vertex, and w is the weight of the edge. The function should take as input a list of edges and the number of vertices in the graph, and return a list of shortest distances from the source vertex to all other vertices. If the graph contains a negative weight cycle, the function should detect it and return a message indicating that the graph contains a negative weight cycle.
"""

def bellman_ford(edges, num_vertices, source):
    """
    This function implements the Bellman-Ford algorithm to find the shortest path 
    from a source vertex to all other vertices in a weighted graph.

    Args:
    edges (list): A list of edges, where each edge is represented as a tuple (u, v, w) 
                  where u is the source vertex, v is the destination vertex, and w is the weight of the edge.
    num_vertices (int): The number of vertices in the graph.
    source (int): The source vertex.

    Returns:
    list: A list of shortest distances from the source vertex to all other vertices. 
          If the graph contains a negative weight cycle, the function returns a message 
          indicating that the graph contains a negative weight cycle.
    """

    # Initialize the distance of the source vertex to 0 and the distance of all other vertices to infinity.
    distances = [float('inf')] * num_vertices
    distances[source] = 0

    # Relax the edges V-1 times (where V is the number of vertices in the graph)
    for _ in range(num_vertices - 1):
        for u, v, w in edges:
            # Update the distance to v if a shorter path is found
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    # Check for negative weight cycles
    for u, v, w in edges:
        # If a shorter path is found after V-1 iterations, there is a negative weight cycle
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            return "Graph contains a negative weight cycle"

    return distances