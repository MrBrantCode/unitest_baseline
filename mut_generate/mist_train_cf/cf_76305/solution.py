"""
QUESTION:
Create a function named `min_reorder(n, connections)` that determines the minimum number of operations required to connect all computers in a network represented by `connections`, where `n` is the number of computers. The function should return `-1` if it is impossible to connect all computers. The constraints are as follows: `1 <= n <= 10^5`, `1 <= connections.length <= min(n*(n-1)/2, 10^5)`, and each connection is a unique pair of distinct computers.
"""

from collections import defaultdict

def min_reorder(n, connections):
    G = defaultdict(list)
    
    # construct the graph
    for comp1, comp2 in connections:
        G[comp1].append(comp2)
        G[comp2].append(comp1)

    # To keep track of visited computers
    visited = [0]*n

    # DFS function
    def dfs(node): 
        visited[node] = 1
        return sum(dfs(i) for i in G[node] if not visited[i]) + 1

    # return -1 if the graph is not complete and return the minimum number of operations otherwise
    return -1 if any(dfs(i) == 0 for i in range(n)) else len(connections) - n + 1