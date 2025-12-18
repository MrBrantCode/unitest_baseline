"""
QUESTION:
Implement a function `BellmanFord(graph, V, E, src)` that takes a weighted graph, the number of vertices `V`, the number of edges `E`, and a source vertex `src` as input, and returns the shortest distances from the source vertex to all other vertices. The graph is represented as an edge list where each edge is represented as `[u, v, w]` where `u` is the source vertex, `v` is the destination vertex, and `w` is the weight of the edge. The function should handle negative edges and detect negative weight cycles. If a negative weight cycle is detected, it should print "Graph contains negative weight cycle" and return, otherwise it should print "No negative weight cycle found" and print the shortest distances. The time complexity of the function should be O(|V||E|) and the space complexity should be O(V).
"""

def BellmanFord(graph, V, E, src):
    # Initialize distance from src to all other vertices as INFINITE
    dis = [float("Inf")] * V
    dis[src] = 0

    # Relax all edges |V| - 1 times.
    for i in range(V - 1):
        for j in range(E):
            if(dis[graph[j][0]] + graph[j][2] < dis[graph[j][1]]):
                dis[graph[j][1]] = dis[graph[j][0]] + graph[j][2]

    # Check for negative-weight cycles.
    for i in range(E):
        x = graph[i][0]    
        y = graph[i][1]    
        weight = graph[i][2]    
        if(dis[x] != float("Inf") and dis[x] + weight < dis[y]):    
            print("Graph contains negative weight cycle") 
            return
        
    print("No negative weight cycle found")
    print(' '.join(str(i) for i in dis))