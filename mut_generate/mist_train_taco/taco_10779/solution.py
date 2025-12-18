"""
QUESTION:
Given a connected undirected graph of N edges and M vertices. The task is the find the total number of spanning trees possible in the graph.
Note: A spanning tree is a subset of Graph G, which has all the vertices covered with the minimum possible number of edges. Hence, a spanning tree does not have cycles and it cannot be disconnected. By this definition, we can draw a conclusion that every connected and undirected Graph G has at least one spanning tree.
Example 1:
Input:
N = 6, M = 5
graph = {{0, 3}
         {0, 1}
         {1, 2}.
         {1, 5},
         {3, 4}}
Output: 1
Explanation: 
Only one spanning tree is possible,i.e. the graph itself.
{{0, 1},
 {0, 3},
 {1, 2},
 {1, 5},
 {3, 4}}
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function countSpanningTrees() which takes two integers N and M and a 2D matrix denoting the connected edges and returns an integers as output.
 
Expected Time Complexity: O(N^{4})
Expected Auxiliary Space: O(N^{2})
 
Constraints:
1 <= N <= 10
N - 1 <= M <= N *(N - 1) / 2
0 <= graph[i][0], graph[i][1] <= N - 1
"""

from typing import List
import numpy as np

def count_spanning_trees(n: int, m: int, graph: List[List[int]]) -> int:
    # Initialize the indegree array and the Laplacian matrix
    indegree = [0] * n
    laplacian = np.zeros(shape=(n, n))
    
    # Fill the indegree array and the Laplacian matrix
    for edge in graph:
        u, v = edge
        indegree[u] += 1
        indegree[v] += 1
        laplacian[u][v] = -1
        laplacian[v][u] = -1
    
    # Fill the diagonal of the Laplacian matrix with the indegree values
    for i in range(n):
        laplacian[i, i] = indegree[i]
    
    # Calculate the cofactor of the Laplacian matrix
    cofactor = round(np.linalg.det(laplacian[1:, 1:]))
    
    # Return the number of spanning trees
    return int(cofactor)