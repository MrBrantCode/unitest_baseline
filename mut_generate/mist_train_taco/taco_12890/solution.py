"""
QUESTION:
Given an undirected Connected graph of V vertices and E edges.
A critical connection is an edge that, if removed, will make some nodes unable to reach some other nodes. Find all critical connections in the graph.
Note: There are many possible orders for the answer. You are supposed to print the edges in sorted order, and also an edge should be in sorted order too. So if there's an edge between node 1 and 2, you should print it like (1,2) and not (2,1).
Example 1:
Input:
Output:
0 1
0 2
Explanation: 
Both the edges in the graph are Crtical
connections.
Example 2:
Input:
Output:
2 3
Explanation:
The edge between nodes 2 and 3 is the only
Critical connection in the given graph.
Your task:
You dont need to read input or print anything. Your task is to complete the function criticalConnections() which takes the integer V denoting the number of vertices and an adjacency list adj as input parameters and returns  a list of lists containing the Critical connections in the sorted order.
Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)
Constraints:
1 ≤ V, E ≤ 10^{5}
"""

def find_critical_connections(V, adj):
    def dfs(sv, parent, low, tin, bridges, vis, timer):
        vis.add(sv)
        tin[sv] = low[sv] = timer
        timer += 1
        for nbr in adj[sv]:
            if nbr == parent:
                continue
            if nbr not in vis:
                dfs(nbr, sv, low, tin, bridges, vis, timer)
                low[sv] = min(low[nbr], low[sv])
                if tin[sv] < low[nbr]:
                    bridges.append([sv, nbr])
            else:
                low[sv] = min(low[nbr], low[sv])
        return

    tin = [0 for _ in range(V)]
    low = [0 for _ in range(V)]
    bridges = []
    vis = set()
    timer = 1
    
    for i in range(V):
        if i not in vis:
            dfs(i, -1, low, tin, bridges, vis, timer)
    
    for ele in bridges:
        ele.sort()
    bridges.sort()
    
    return bridges