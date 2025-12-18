"""
QUESTION:
Write a function called `find_negative_cycles` that takes a weighted graph represented as an adjacency matrix and returns all negative cycles in the graph. The graph may contain multiple negative cycles, and the function should find and return all of them. Note that the graph is represented as a 2D array where `graph[i][j]` is the weight of the edge from node `i` to node `j`. If there is no edge between nodes `i` and `j`, `graph[i][j]` is assumed to be infinity.
"""

import sys

def find_negative_cycles(graph):
    """
    Finds all negative cycles in a weighted graph represented as an adjacency matrix.

    Args:
    graph (list of lists): A 2D array where graph[i][j] is the weight of the edge from node i to node j.
    
    Returns:
    list: A list of lists, where each sublist contains a negative cycle in the graph.
    """

    # Initialize distance matrix
    distance = [[float('inf')] * len(graph) for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
            distance[i][j] = graph[i][j]
    
    # Floyd-Warshall algorithm
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    # Check for negative cycles
    negative_cycles = []
    for i in range(len(graph)):
        if distance[i][i] < 0:
            negative_cycles.append([i])

    # For each negative cycle found, try to construct the cycle by backtracking
    for cycle in negative_cycles:
        start = cycle[0]
        for k in range(len(graph)):
            if distance[start][k] + distance[k][start] == distance[start][start]:
                cycle.append(k)
                cycle.append(start)
                break

    return negative_cycles