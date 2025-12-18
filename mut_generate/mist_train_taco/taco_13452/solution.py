"""
QUESTION:
Eulerian Path is a path in a graph that visits every edge exactly once. Eulerian Circuit is an Eulerian Path that starts and ends on the same vertex. Given the number of vertices V and adjacency list adj denoting the graph. Your task is to find that there exists the Euler circuit or not
Note that: Given graph is connected.
Example 1:
Input: 
Output: 1
Explanation: One of the Eularian circuit 
starting from vertex 0 is as follows:
0->1->3->2->0
 
Your Task:
You don't need to read or print anything. Your task is to complete the function isEularCircuitExist() which takes V and adjacency list adj as input parameter and returns boolean value 1 if Eular circuit exists otherwise returns 0.
 
Expected Time Complexity: O(V + E)
Expected Space Complexity: O(V)
 
Constraints:
1 <= V <= 10^{5}
1 <= E <= 2*10^{5}
"""

def is_eulerian_circuit_exists(V, adj):
    def dfs(node, visited, adj):
        visited[node] = 1
        for nbr in adj[node]:
            if visited[nbr] == -1:
                dfs(nbr, visited, adj)

    def connected_graph(visited, adj, V):
        start = -1
        for i in range(V):
            if len(adj[i]):
                start = i
                break
        if start == -1:
            return True
        dfs(start, visited, adj)
        for i in range(V):
            if visited[i] == -1 and len(adj[i]) > 0:
                return False
        return True

    visited = [-1] * V
    if not connected_graph(visited, adj, V):
        return 0
    for i in range(V):
        if len(adj[i]) % 2 != 0:
            return 0
    return 1