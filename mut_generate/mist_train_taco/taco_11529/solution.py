"""
QUESTION:
There are a total of N tasks, labeled from 0 to N-1. Some tasks may have prerequisites, for example to do task 0 you have to first complete task 1, which is expressed as a pair: [0, 1]
Given the total number of tasks N and a list of prerequisite pairs P, find if it is possible to finish all tasks.
Example 1:
Input: 
N = 4, P = 3
prerequisites = {{1,0},{2,1},{3,2}}
Output:
Yes
Explanation:
To do task 1 you should have completed
task 0, and to do task 2 you should 
have finished task 1, and to do task 3 you 
should have finished task 2. So it is possible.
Example 2:
Input:
N = 2, P = 2
prerequisites = {{1,0},{0,1}}
Output:
No
Explanation:
To do task 1 you should have completed
task 0, and to do task 0 you should
have finished task 1. So it is impossible.
Your task:
You don’t need to read input or print anything. Your task is to complete the function isPossible() which takes the integer N denoting the number of tasks, P denoting the number of prerequisite pairs and prerequisite as input parameters and returns true if it is possible to finish all tasks otherwise returns false. 
Expected Time Complexity: O(N + P)
Expected Auxiliary Space: O(N + P)
Constraints:
1 ≤ N ≤ 10^{4}
1 ≤ P ≤ 10^{5}
"""

from queue import Queue

def can_finish_tasks(N, prerequisites):
    V = N
    adj = [[] for _ in range(V)]
    
    # Build the adjacency list
    for (edge, vertex) in prerequisites:
        adj[vertex].append(edge)
    
    # Initialize indegree array
    indegree = [0] * V
    
    # Calculate indegree for each vertex
    for i in range(V):
        for j in range(len(adj[i])):
            indegree[adj[i][j]] += 1
    
    # Initialize queue with all vertices with indegree 0
    q = Queue()
    for i in range(V):
        if indegree[i] == 0:
            q.put(i)
    
    visited = 0
    
    # Process the queue
    while not q.empty():
        var = q.get()
        visited += 1
        for i in range(len(adj[var])):
            indegree[adj[var][i]] -= 1
            if indegree[adj[var][i]] == 0:
                q.put(adj[var][i])
    
    # If all tasks can be visited, return True, else False
    return visited == V