"""
QUESTION:
Given an undirected graph with V vertices. We say two vertices u and v belong to a single province if there is a path from u to v or v to u. Your task is to find the number of provinces.
Note:  A province is a group of directly or indirectly connected cities and no other cities outside of the group. 
Example 1:
Input:
[
 [1, 0, 1],
 [0, 1, 0],
 [1, 0, 1]
]
Output:
2
Explanation:
The graph clearly has 2 Provinces [1,3] and [2]. As city 1 and city 3 has a path between them they belong to a single province. City 2 has no path to city 1 or city 3 hence it belongs to another province.
Example 2:
Input:
[
 [1, 1],
 [1, 1]
]
Output :
1
Your Task:  
You don't need to read input or print anything. Your task is to complete the function numProvinces() which takes an integer V and an adjacency matrix adj as input and returns the number of provinces. adj[i][j] = 1, if nodes i and j are connected and adj[i][j] = 0, if not connected.
Expected Time Complexity: O(V^{2})
Expected Auxiliary Space: O(V)
Constraints:
1 ≤ V ≤ 500
"""

def count_provinces(adj_matrix, V):
    def make_adj(mat):
        adj = [[] for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and i != j:
                    adj[i].append(j)
        return adj

    def dfs(adj, s, visited):
        visited[s] = True
        for u in adj[s]:
            if not visited[u]:
                dfs(adj, u, visited)

    def dfs_connected(adj):
        visited = [False] * len(adj)
        count = 0
        for u in range(len(adj)):
            if not visited[u]:
                count += 1
                dfs(adj, u, visited)
        return count

    adj_edges = make_adj(adj_matrix)
    return dfs_connected(adj_edges)