"""
QUESTION:
Given a connected acyclic graph with n nodes and n-1 edges, count the pair of nodes that are at even distance(number of edges) from each other.
Example 1:
Input:
n = 3
graph = {{}, {2}, {1, 3}, {2}}
Output: 1
Explaination: Here there are three pairs {1,2},{1,3}
and {2,3} and only {1,3} has even distance between them.
i.e           1
             /
            2
           /
          3
Example 2:
Input:
n = 5
graph = {{}, {2,4}, {1,3}, {2}, {1,5}, {4}}
Output: 4
Explaination: There are four pairs {1,3},{1,5},{2,4}
and {3,5} which has even distance.
Your Task:
You don't need to read input or print anything. Your task is to complete the function countOfNodes() which takes the array graph[] (given as Adjacency list) and its size n as input parameters and returns the count of pair of nodes that are at even distance from each other
Expected Time Complexity: O(V+E)
Expected Auxiliary Space: O(V)
Constraints:
1 ≤ n ≤ 10^{4}
"""

from collections import deque

def bfs(visit, graph, level, i):
    visit[i] = 1
    q = deque()
    q.append([i, 0])
    while q:
        t = q.popleft()
        u = t[0]
        lev = t[1]
        if lev not in level:
            level[lev] = [u]
        else:
            level[lev].append(u)
        for v in graph[u]:
            if visit[v] == 0:
                visit[v] = 1
                q.append([v, lev + 1])

def count_even_distance_pairs(graph, n):
    visit = [0] * (n + 1)
    level = {}
    for i in range(1, n + 1):
        if visit[i] == 0:
            bfs(visit, graph, level, i)
    odd = 0
    even = 0
    for i in level:
        if i % 2 == 0:
            even += len(level[i])
        else:
            odd += len(level[i])
    ans = even * (even - 1) // 2 + odd * (odd - 1) // 2
    return ans