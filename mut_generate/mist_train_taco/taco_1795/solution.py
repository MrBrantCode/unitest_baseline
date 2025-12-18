"""
QUESTION:
Reverse Delete algorithm is closely related to Kruskal’s algorithm. In Reverse Delete algorithm, we sort all edges in decreasing order of their weights. After sorting, we one by one pick edges in decreasing order. We include current picked edge if excluding current edge causes disconnection in current graph. The main idea is delete edge if its deletion does not lead to disconnection of graph. Your task is to print the value of total weight of Minimum Spanning Tree formed.
 
Example 1:
Input:
V = 4, E = 5
Arr[] = {0, 1, 10, 0, 2, 6, 0, 3, 5, 1, 3, 15, 2, 3, 4}
Output:
19
Explanation:
The weight of the Minimum Spanning
Tree formed is 19.
Example 1:
Input:
V = 4, E = 3
Arr[] = {0, 1, 98, 1, 3, 69, 0, 3, 25}
Output:
192
Explanation:
The weight of the Minimum Spanning
Tree formed is 192.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function RevDelMST() which takes 2 Integers V, and E and an array of length 3*E where each triplet consists of two nodes u and v and weight of thir edge w as input and returns the Weight of the Minimum Spanning Tree.
 
Expected Time Complexity: O(V*E)
Expected Auxiliary Space: O(E)
 
Constraints:
1 <= V,E <= 1000
1 <= u,v <= V
1 <= w <= 100
"""

from collections import defaultdict

def reverse_delete_mst(V, E, edges):
    def dfs(node, visited, adj):
        visited[node] = 1
        for nbr in adj[node]:
            if visited[nbr] == -1:
                dfs(nbr, visited, adj)

    def is_connected(V, adj):
        visited = [-1] * V
        cnt = 0
        for i in range(V):
            if visited[i] == -1:
                dfs(i, visited, adj)
                cnt += 1
        return cnt == 1

    adj = defaultdict(list)
    for (u, v, w) in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    edges.sort(key=lambda x: -x[2])
    cost = 0
    
    for (u, v, w) in edges:
        adj[u].remove(v)
        adj[v].remove(u)
        if not is_connected(V, adj):
            adj[u].append(v)
            adj[v].append(u)
            cost += w
    
    return cost