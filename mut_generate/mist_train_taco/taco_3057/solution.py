"""
QUESTION:
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.
Example 1:
Input:
Output: 1
Explanation: 3 -> 3 is a cycle
Example 2:
Input:
Output: 0
Explanation: no cycle in the graph
Your task:
You dont need to read input or print anything. Your task is to complete the function isCyclic() which takes the integer V denoting the number of vertices and adjacency list adj as input parameters and returns a boolean value denoting if the given directed graph contains a cycle or not.
In the adjacency list adj, element adj[i][j] represents an edge from i to j.
Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)
Constraints:
1 ≤ V, E ≤ 10^{5}
"""

def is_cyclic(V, adj):
    def dfs_cycle(adj, a, visited, dfs_call):
        if a in visited and a in dfs_call:
            return True
        elif a not in visited:
            visited.add(a)
            dfs_call.add(a)
            for i in adj[a]:
                if dfs_cycle(adj, i, visited, dfs_call):
                    return True
            dfs_call.remove(a)
        return False

    visited = set()
    dfs_call = set()
    for a in range(V):
        if a not in visited:
            if dfs_cycle(adj, a, visited, dfs_call):
                return True
    return False