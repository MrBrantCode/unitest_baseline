"""
QUESTION:
Given a directed acyclic graph(DAG) with n nodes labeled from 0 to n-1. Given edges, s and d ,count the number of ways to reach from s to d.There is a directed Edge from vertex edges[i][0] to the vertex edges[i][1].
 
Example:
Input: edges = {{0,1},{0,3},{1,2},{3,2}}, 
n = 4, s = 0, d = 2
Output: 2
Explanation: There are two ways to reach at 
2 from 0. These are-
1. 0->1->2
2. 0->3->2
 
Your Task:
You don't need to read or print anything. Your task is to complete the function possible_paths() which takes edges, n, s and d as input parameter and returns the number of ways to reach from s to d.
 
Expected Time Compelxity: O(2^{n})
Expected Space Complexity: O(n+e) 
where e is the number of edges in the graph.
 
Constraints:
1 <= n <= 15
0 <= s, d <= n-1
"""

def count_paths(edges, n, s, d):
    # Create an adjacency list for the graph
    g = [[] for _ in range(n)]
    for (a, b) in edges:
        g[a].append(b)
    
    # Set to store unique paths
    path = set()
    
    # Helper function to perform DFS and count paths
    def helper(node, prev, p):
        if node == d:
            path.add(tuple(p + [node]))
            return
        if node in p:
            return
        for neig in g[node]:
            if neig != prev:
                helper(neig, node, p + [node])
    
    # Start the DFS from the source node
    helper(s, -1, [])
    
    # Return the number of unique paths
    return len(path)