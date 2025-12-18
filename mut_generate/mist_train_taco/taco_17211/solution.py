"""
QUESTION:
There are M job applicants and N jobs.  Each applicant has a subset of jobs that he/she is interseted in. Each job opening can only accept one applicant and a job applicant can be appointed for only one job. Given a matrix G where G(i,j) denotes i^{th }applicant is interested in j^{th }job. Find an assignment of jobs to applicant in such that as many applicants as possible get jobs.
 
Example 1:
Input: G = {{1,1,0,1,1},{0,1,0,0,1},
{1,1,0,1,1}}
Output: 3
Explanation: There is one of the possible
assignment-
First applicant gets the 1st job.
Second applicant gets the 2nd job.
Third applicant gets the 3rd job.
Example 2:
Input: G = {{1,1},{0,1},{0,1},{0,1},
{0,1},{1,0}}
Output: 2
Explanation: There is one of the possible
assignment-
First applicant gets the 1st job.
Second applicant gets the 2nd job.
 
Your Task:
You don't need to read to print anything. Your task is to complete the function maximumMatch() which takes matrix G as input parameter and returns the maximum number of applicants who can get the job.
 
Expected Time Complexity: O(N^{3})
Expected Auxiliary Space: O(N)
 
Constraints:
1 ≤ N, M ≤ 100
"""

def maximum_match(G):
    def BFS(G, parent, s, t):
        n = len(G)
        visited = [False for _ in range(n)]
        queue = deque()
        queue.append(s)
        visited[s] = True
        while queue:
            vertex = queue.popleft()
            for neighbour in range(n):
                if not visited[neighbour] and G[vertex][neighbour] > 0:
                    queue.append(neighbour)
                    visited[neighbour] = True
                    parent[neighbour] = vertex
                    if neighbour == t:
                        return True
        return False

    def augment_the_path(G, parent, vertex):
        bottle_neck = float('inf')
        help_variable = vertex
        while parent[vertex] is not None:
            bottle_neck = min(bottle_neck, G[parent[vertex]][vertex])
            vertex = parent[vertex]
        vertex = help_variable
        while parent[vertex] is not None:
            G[parent[vertex]][vertex] -= bottle_neck
            G[vertex][parent[vertex]] += bottle_neck
            vertex = parent[vertex]
        return bottle_neck

    def ford_fulkerson(M, s, t):
        n = len(M)
        max_flow = 0
        parent = [None for _ in range(n)]
        while BFS(M, parent, s, t):
            bottle_neck = augment_the_path(M, parent, t)
            max_flow += bottle_neck
        return max_flow

    def create_vertices(Graph):
        n = len(Graph[0])
        m = len(Graph)
        size = n + m + 2
        G = [[0 for _ in range(n + m + 2)] for _ in range(n + m + 2)]
        for guy in range(m):
            G[size - 2][guy] = 1
            for machine in range(n):
                if Graph[guy][machine] == 1:
                    G[guy][m + machine] = 1
        for machine in range(n):
            G[m + machine][size - 1] = 1
        return ford_fulkerson(G, size - 2, size - 1)

    return create_vertices(G)