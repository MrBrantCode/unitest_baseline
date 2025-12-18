"""
QUESTION:
Given a weighted graph of N vertices numbered from 0 to N-1 in the form of adjacency matrix A[ ][ ] and two integers S denoting the number of source vertex and T denoting the number of sink vertex. The task is to find minimum capacity s-t cut of the given network. An s-t cut is a cut that requires the source node ‘S’ and the sink node ‘T’ to be in different subsets, and it consists of edges going from the source’s side to the sink’s side. The capacity of an s-t cut is defined by the sum of the capacity of each edge in the cut-set. In other words, you have to find out all the edges which has to be removed to make it impossible to reach the sink node from source node, and the edges you select should have a minimum sum of weights. You have to return all the edges included in the minimum capacity s-t cut and if there are no edges in minimum capacity s-t cut, return "-1".
Example 1:
Input:
N = 2
A[][] = [[0, 3],
         [0, 0]]
S = 0
T = 1
Output:
0 1
Explanation: We have to remove the edge going
from 0^{th} vertex to 1^{st} vertex.
 
Example 2:
Input:
N = 5
A[][] = [[0, 0, 0, 0, 0],
         [0, 0, 2, 3, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]
S = 0
T = 4
Output:
-1
Explanation: There are no edges in 
minimum capacity s-t cut.
Your Task: 
You don't need to read input or print anything. Your task is to complete the function minimumCut() which takes the adjacency matrix A[ ][ ], source node number S, sink node number T and number of vertices N and returns a list of integers res[ ] where res[2*i-1] and res[2*i] denotes an edge in minimum capacity s-t cut where 1 ≤ i ≤ length(res)/2, if there are no edges in minimum capacity s-t cut, return only one integer "-1" in res[ ].
Expected Time Complexity: O(max_flow * N^{2})
Expected Auxiliary Space: O(N^{2})
Constraints:
1 ≤ N ≤ 50
0 ≤ S, T < N
"""

def find_minimum_cut(A, S, T, N):
    def BFS(graph, s, t, parent):
        visited = [False] * N
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(graph[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return visited[t]

    def dfs(graph, s, visited):
        visited[s] = True
        for i in range(len(graph)):
            if graph[s][i] > 0 and not visited[i]:
                dfs(graph, i, visited)

    graph = [row[:] for row in A]
    parent = [-1] * N
    max_flow = 0
    s = -1

    while BFS(graph, S, T, parent):
        path_flow = float('Inf')
        s = T
        while s != S:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = T
        while v != S:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    if s != -1:
        visited = [False] * N
        dfs(graph, S, visited)
        cut_list = []
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 0 and A[i][j] > 0 and visited[i]:
                    cut_list.append(f"{i} {j}")
        return cut_list if cut_list else ["-1"]
    return ["-1"]