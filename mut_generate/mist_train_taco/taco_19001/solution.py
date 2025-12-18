"""
QUESTION:
Given an integer N, denoting the number of computers connected by cables forming a network and a 2d array connections[][], with each row (i, j) representing a connection between i^{th} and j^{th} computer, the task is to connect all the computers either directly or indirectly by removing any of the given connections and connecting two disconnected computers. 
If its not possible to connect all the computers, print -1. 
Otherwise, print the minimum number of such operations required.
Example 1:
Input:
N = 4 
connections[][] = {{0, 1}, {0, 2}, {1, 2}}
Output:
1
Explanation: 
Remove the connection between computers 1 and 2 and connect computers 1 and 3.
Example 2:
Input:
N = 5
connections[][] = {{0, 1}, {0, 2}, {3, 4}, {2, 3}}
Output:
0
Explanation:
No removal of connections is required.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function minimizeConnections() which takes the array connections[], number of computers N as input parameters and returns the minimum number of operations required to connect all computers with each other. If it is not possible to do so then return -1.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{3}
0<=connections[i][0],connections[i][1]
"""

from typing import List

def minimizeConnections(N: int, connections: List[List[int]]) -> int:
    # Create adjacency list
    adj = [[] for _ in range(N)]
    for (i, j) in connections:
        adj[i].append(j)
        adj[j].append(i)

    # DFS function to traverse the graph
    def dfs(i):
        q = [i]
        while q:
            s = q.pop(0)
            for nei in adj[s]:
                if not visited[nei]:
                    visited[nei] = True
                    q.append(nei)

    # Initialize visited array
    visited = [False] * N
    count = 0

    # Count the number of connected components
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(i)
            count += 1

    # Calculate redundant connections
    redundant = len(connections) - (N - 1)
    if redundant >= 0:
        return count - 1
    return -1