"""
QUESTION:
Given N nodes of a tree and a list of edges. Find the minimum number of nodes to be selected to light up all the edges of the tree.
An edge lights up when at least one node at the end of the edge is selected.
Example 1:
Input:
N = 6
edges[] = {(1,2), (1,3), (2,4), (3,5), (3,6)}
Output: 2
Explanation: Selecting nodes 2 and 3 lights
up all the edges.
Example 2:
Input:
N = 3
arr[] = {(1,2), (1,3)}
Output: 1
Explanation: Selecting Node 1 
lights up all the edges.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function countVertex() which takes the number of nodes N, and the list of edges as input parameters and returns the minimum number of nodes selected.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ edges ≤ N
Given graph is a valid tree.
"""

def count_min_nodes_to_light_tree(N, edges):
    def dfs(graph, u, p):
        (exc, inc) = (0, 1)
        for v in graph[u]:
            if v != p:
                (cexc, cinc) = dfs(graph, v, u)
                exc += cinc
                inc += min(cinc, cexc)
        return (exc, inc)

    graph = [[] for _ in range(N)]
    for (u, v) in edges:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    
    return min(dfs(graph, 0, -1))