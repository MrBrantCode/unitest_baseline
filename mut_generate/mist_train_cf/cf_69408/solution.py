"""
QUESTION:
Write a function `dijkstra` that takes in a weighted graph represented as an adjacency matrix, a source vertex, and a destination vertex. The function should return the shortest distance between the source vertex and the destination vertex using Dijkstra's algorithm. The graph is represented as a 2D list where graph[i][j] represents the weight between node i and node j, and a weight of 0 indicates no direct edge between nodes.
"""

import sys

def dijkstra(graph, src_vertex, dest_vertex):
    vertices_count = len(graph)

    distances = [sys.maxsize] * vertices_count
    distances[src_vertex] = 0

    visited = [False] * vertices_count

    for _ in range(vertices_count):
        min_val = sys.maxsize
        min_index = -1 

        for v in range(len(distances)):
            if distances[v] < min_val and visited[v] == False:
                min_val = distances[v]
                min_index = v

        visited[min_index] = True

        for v in range(vertices_count):
            if (graph[min_index][v] > 0 and
                visited[v] == False and
                distances[v] > distances[min_index] + graph[min_index][v]):
                distances[v] = distances[min_index] + graph[min_index][v]

    return distances[dest_vertex]