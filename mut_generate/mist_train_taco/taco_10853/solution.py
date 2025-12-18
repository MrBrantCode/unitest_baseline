"""
QUESTION:
Given a Directed Graph with V vertices and E edges,  Find the members of strongly connected components in the graph.
Example 1:
Input:
Output:
0 1 2,3,4,
Explanation:
We can clearly see that there are 3 Strongly
Connected Components in the Graph as mentioned
in the Output.
Example 2:
Input:
Output:
0 1 2,
Explanation:
All of the nodes are connected to each other.
So, there's only one SCC as shown.
Your Task:
You don't need to read input or print anything. Your task is to complete the function tarjans() which takes the number of vertices V and adjacency list of the graph as input parameters and returns a list of list of integers denoting the members of strongly connected components in the given graph.
Note: A single strongly connected component must be represented in the form of a list if integers sorted in the ascending order. The resulting list should consist of a list of all SCCs which must be sorted in a way such that a lexicographically smaller list of integers appears first. 
Expected Time Complexity: O(V + E).
Expected Auxiliary Space: O(V).
Constraints:
1  ≤  V  ≤  10^{5}
1  ≤  E  ≤  10^{5}
0  ≤  u, v  ≤  N-1
"""

def find_strongly_connected_components(V, adj):
    def dfs(node, parent, adj, disc, low, stk, in_stk, scc):
        disc[node] = low[node] = timer[0]
        timer[0] += 1
        stk.append(node)
        in_stk[node] = True
        for nbr in adj[node]:
            if disc[nbr] == -1:
                dfs(nbr, node, adj, disc, low, stk, in_stk, scc)
                low[node] = min(low[node], low[nbr])
            elif in_stk[nbr]:
                low[node] = min(low[node], disc[nbr])
        if low[node] == disc[node]:
            temp = []
            u = -1
            while u != node:
                u = stk.pop()
                temp.append(u)
                in_stk[u] = False
            temp.sort()
            scc.append(temp)

    disc = [-1] * V
    low = [-1] * V
    timer = [0]
    stk = []
    in_stk = [False] * V
    scc = []
    for i in range(V):
        if disc[i] == -1:
            dfs(i, -1, adj, disc, low, stk, in_stk, scc)
    scc.sort()
    return scc