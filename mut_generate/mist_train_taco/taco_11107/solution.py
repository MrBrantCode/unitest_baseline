"""
QUESTION:
Given a Undirected Graph with V vertices and E edges, Find the level of node X. if X does not exist in the graph then print -1.
Note: Traverse the graph starting from vertex 0.
  
Example 1:
Input:
X = 4
Output:
2
Explanation:
We can clearly see that Node 4 lies at Level 2.
Example 2:
Input:
X = 5
Output:
-1
Explanation:
Node 5 isn't present in the Graph, so the
Output is -1.
 
Your task:
You dont need to read input or print anything. Your task is to complete the function nodeLevel() which takes two integers V and X denoting the number of vertices and the node, and another adjacency list adj as input parameters and returns the level of Node X. If node X isn't present it returns -1.
Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)
 
Constraints:
2  ≤  V  ≤  10^{4}
1  ≤  E  ≤  (N*(N-1))/2
0  ≤ u, v < V
1  ≤  X  ≤  10^{4}
Graph doesn't contain multiple edges and self loops.
"""

import queue

def find_node_level(V, adjList, X):
    vis = [-1] * V
    s = queue.Queue()
    src = 0
    count = 0
    s.put([count, src])
    
    while not s.empty():
        (count, node) = s.get()
        if node == X:
            return count
        for i in adjList[node]:
            if i == X:
                return count + 1
            if vis[i] == -1:
                s.put([count + 1, i])
                vis[i] = 1
    
    return -1