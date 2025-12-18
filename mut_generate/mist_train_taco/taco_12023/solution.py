"""
QUESTION:
Given a Directed Acyclic Graph having V vertices and E edges, where each edge {U, V} represents the Jobs U and V such that Job V can only be started only after completion of Job U. The task is to determine the minimum time taken by each job to be completed where each Job takes unit time to get completed.
Example 1:
Input:
N=10
M=13
edges[]={{1,3},{1,4},{1,5},{2,3},{2,8},{2,9},{3,6},{4,6},{4,8},{5,8},{6,7},{7,8},{8,10}}
Output:
time[]={1,1,2,2,2,3,4,5,2,6 }
Explanation:
Start jobs 1 and 2 at the beginning and complete them at 1 unit of time. 
Since, all the jobs on which need to be completed before the jobs 3, 4, 5, and 9 are completed. So, we can start these jobs at 1st unit of time and complete these at 2nd unit of time after the completion of the dependent Job.
Similarly, 
Job 6 can only be done after the 3rd and 4th jobs are done. So, start it at the 2nd unit of time and complete it at the 3rd unit of time.
Job 7 can only be done after job 6 is done. So, you can start it at the 3rd unit of time and complete it at the 4th unit of time.
Job 8 can only be done after the 4th, 5th, and 7th jobs are done. So, start it at the 4th unit of time and complete it at the 5th unit of time.
Job 10 can only be done after the 8th job is done. So, start it at the 5th unit of time and complete it at the 6th unit of time.
Example2:
Input:
N=7
M=7
edges[]={{1,2},{2,3},{2,4},{2,5},{3,6},{4,6},{5,7}}
Output:
time[]={1,2,3,3,3,4,4}
Explanation:
Start Job 1 at the beginning and complete it at 1st unit of time.
Job 2 can only be done after 1st Job is done. So, start it at 1st unit of time and complete it at 2nd unit of time.
Since, Job 3, 4, and 5 have the only dependency on the 2nd Job. So, start these jobs at the 2nd unit of time and complete these at the 3rd unit of time.
Job 6 can only be done after the 3rd and 4th Job is done. So, start it at the 3rd unit of time and complete it at the 4th unit of time.
Job 7 can only be done after the 5th Job is done. So, start it at the 3rd hour and complete it at the 4th unit of time.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function minimumTime() which takes the edge list e[] of the graph, its size number of nodes N and M the number of edges as input parameters and returns the time array.
 
Expected Time Complexity: O(V+E), where V is the number of nodes and E is the number of edges. 
Expected Auxiliary Space: O(V)
 
Constraints:
1 <= N <= 10^{3}
1<=M<=N*(N-1)/2
1<=edges[i][0],edges[i][1]<=N.
"""

from typing import List
from collections import defaultdict, deque

def minimum_time_to_complete_jobs(n: int, m: int, edges: List[List[int]]) -> List[int]:
    graph = defaultdict(list)
    incoming = [0] * (n + 1)
    
    # Build the graph and count incoming edges for each node
    for (u, v) in edges:
        graph[u].append(v)
        incoming[v] += 1
    
    # Initialize the queue with nodes having no incoming edges
    queue = deque()
    for idx in range(1, n + 1):
        if incoming[idx] == 0:
            queue.append(idx)
    
    # Initialize the result array with zeros
    time_to_complete = [0] * (n + 1)
    current_time = 1
    
    # Perform topological sort using Kahn's algorithm
    while queue:
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            time_to_complete[node] = current_time
            for neighbor in graph[node]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    queue.append(neighbor)
        current_time += 1
    
    # Return the result excluding the 0th index (dummy index)
    return time_to_complete[1:]