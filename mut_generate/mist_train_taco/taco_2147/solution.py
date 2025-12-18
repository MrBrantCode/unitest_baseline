"""
QUESTION:
Given an undirected graph (not necessarily connected) with V vertices and adjacency list adj. You are required to find all the vertices removing which (and edges through it) disconnects the graph into 2 or more components, or in other words, removing which increases the number of connected components.
Note: Indexing is zero-based i.e nodes numbering from (0 to V-1). There might be loops present in the graph.
Example 1:
Input:
Output:{1,4}
Explanation: Removing the vertex 1 will
discconect the graph as-
Removing the vertex 4 will disconnect the
graph as-
 
Your Task:
You don't need to read or print anything. Your task is to complete the function articulationPoints() which takes V and adj as input parameters and returns a list containing all the vertices removing which turn the graph into two or more disconnected components in sorted order. If there are no such vertices then returns a list containing -1.
 
Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)
 
Constraints:
1 ≤ V ≤ 10^{4}
"""

def find_articulation_points(V, adj):
    visited = [0] * V
    tin = [float('inf')] * V
    low = [float('inf')] * V
    mark = set()
    timer = 1

    def dfs(node, par):
        nonlocal timer
        visited[node] = 1
        tin[node] = low[node] = timer
        timer += 1
        child = 0
        for each in adj[node]:
            if not visited[each]:
                dfs(each, node)
                low[node] = min(low[node], low[each])
                if low[each] >= tin[node] and par != -1:
                    mark.add(node)
                child += 1
            else:
                low[node] = min(low[node], tin[each])
        if child > 1 and par == -1:
            mark.add(node)

    for i in range(V):
        if not visited[i]:
            dfs(i, -1)

    return sorted(list(mark)) if mark else [-1]