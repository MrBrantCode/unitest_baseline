"""
QUESTION:
An IT company is working on a large project. The project is broken into N modules and distributed to different teams. Each team can work parallelly. The amount of time (in months) required to complete each module is given in an array duration[ ] i.e. time needed to complete i^{th} module is duration[i] months. 
You are also given M dependencies such that for each i (1 ≤ i ≤ M)  dependencies[i][1]^{th} module can be started after dependencies[i][0]^{th} module is completed.
As the project manager, compute the minimum time required to complete the project.
Note: It is guaranteed that a module is not dependent on itself.
Example 1:
Input:
N = 6, M = 6
duration[] = {1, 2, 3, 1, 3, 2}
dependencies[][]:
[[5, 2]
 [5, 0]
 [4, 0] 
 [4, 1]
 [2, 3]
 [3, 1]]
Output: 
8
Explanation: 
The Graph of dependency forms this and 
the project will be completed when Module 
1 is completed which takes 8 months.
Example 2:
Input:
N = 3, M = 3
duration[] = {5, 5, 5}
dependencies[][]:
[[0, 1]
 [1, 2]
 [2, 0]]
Output: 
-1
Explanation: 
There is a cycle in the dependency graph 
hence the project cannot be completed.
Your Task:
Complete the function minTime() which takes N, M, duration array, and dependencies array as input parameter and return the minimum time required. return -1 if the project can not be completed. 
Expected Time Complexity: O(N+M)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
0 ≤ M ≤ 2*10^{5}
0 ≤ duration[i] ≤ 10^{5}
0 ≤ dependencies[i][j] < N
"""

def calculate_min_project_completion_time(N, M, duration, dependencies):
    degree = [0] * N
    adj = [[] for _ in range(N)]
    
    for edge in dependencies:
        adj[edge[0]].append(edge[1])
        degree[edge[1]] += 1
    
    dist = [-1] * N
    pq = []
    
    for i in range(N):
        if degree[i] == 0:
            dist[i] = duration[i]
            heapq.heappush(pq, (dist[i], i))
    
    while len(pq) > 0:
        (d, v) = heapq.heappop(pq)
        for w in adj[v]:
            degree[w] -= 1
            if degree[w] == 0:
                dist[w] = d + duration[w]
                heapq.heappush(pq, (dist[w], w))
    
    if -1 in dist:
        return -1
    
    return max(dist)