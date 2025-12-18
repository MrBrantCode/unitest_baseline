"""
QUESTION:
Write a function `solve` that takes four parameters: `n`, `edgeList`, `nodeWeights`, and `queries`. The function should return a boolean array where each value represents whether there is a path between two nodes in the given undirected graph that satisfies the given constraints.

The function should take the following parameters:
- `n`: The number of nodes in the graph.
- `edgeList`: A list of edges in the graph, where each edge is represented as a list `[ui, vi, disi]`, denoting an edge between nodes `ui` and `vi` with distance `disi`.
- `nodeWeights`: A list of node weights, where `nodeWeights[k]` is the weight of node `k`.
- `queries`: A list of queries, where each query is represented as a list `[pj, qj, limitj, weightj]`, and the function should determine whether there is a path between `pj` and `qj` such that each edge on the path has a distance strictly less than `limitj` and the total weight of the nodes on the path is less than `weightj`.

The function should return a boolean array where each value represents the result of the corresponding query.
"""

import heapq

def solve(n, edgeList, nodeWeights, queries):
    """
    This function determines whether there is a path between two nodes in the given undirected graph 
    that satisfies the given constraints.

    Parameters:
    n (int): The number of nodes in the graph.
    edgeList (list): A list of edges in the graph, where each edge is represented as a list [ui, vi, disi], 
                     denoting an edge between nodes ui and vi with distance disi.
    nodeWeights (list): A list of node weights, where nodeWeights[k] is the weight of node k.
    queries (list): A list of queries, where each query is represented as a list [pj, qj, limitj, weightj].

    Returns:
    list: A boolean array where each value represents the result of the corresponding query.
    """
    
    graph = {i: [] for i in range(n)}
    
    for u, v, p in edgeList:
        graph[u].append((v, p))
        graph[v].append((u, p))

    def shortestPath(start, end, limit, weight):
        """
        This function calculates the shortest path between two nodes in the graph.

        Parameters:
        start (int): The starting node.
        end (int): The ending node.
        limit (int): The maximum distance.
        weight (int): The maximum weight.

        Returns:
        bool: Whether there is a path between the two nodes that satisfies the constraints.
        """
        queue = [(0, start, 0)]
        seen = set()

        while queue:
            dist, node, weight_sum = heapq.heappop(queue)
            
            if node == end: return True
            if node in seen: continue

            seen.add(node)
            weight_sum += nodeWeights[node]

            if weight_sum >= weight: continue

            for next_node, edge in graph[node]:
                if edge < limit:
                    heapq.heappush(queue, (dist + edge, next_node, weight_sum))
        
        return False

    return [shortestPath(u, v, limit, weight) for u, v, limit, weight in queries]