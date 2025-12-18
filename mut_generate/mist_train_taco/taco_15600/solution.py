"""
QUESTION:
Given a directed graph, find out if a vertex j is reachable from another vertex i for all vertex pairs (i, j) in the given graph. Here reachable mean that there is a path from vertex i to j. The reach-ability matrix is called transitive closure of a graph. The directed graph is represented by adjacency list graph where there are N vertices.
Example 1:
Input: N = 4
graph = {{1, 1, 0, 1}, 
         {0, 1, 1, 0}, 
         {0, 0, 1, 1}, 
         {0, 0, 0, 1}}
Output: {{1, 1, 1, 1}, 
         {0, 1, 1, 1}, 
         {0, 0, 1, 1}, 
         {0, 0, 0, 1}}
Explaination: The output list shows the 
reachable indexes.
Your Task:
You do not need to read input or print anything. Your task is to complete the function transitiveClosure() which takes N and graph as input parameters and returns the transitive closure of the graph in form of 2d array.
Expected Time Complexity: O(N^{3})
Expected Auxiliary Space: O(N^{2})
Constraints:
1 ≤ N ≤ 100
"""

def transitive_closure(N, graph):
    # Convert adjacency matrix to adjacency list
    g = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and graph[i][j] == 1:
                g[i].append(j)

    # Helper function to perform DFS and find reachable nodes
    def helper(node, prev, seen):
        if node in seen:
            return seen
        seen.add(node)
        for neig in g[node]:
            if neig != prev:
                helper(neig, node, seen)
        return seen

    # Initialize the output transitive closure matrix
    output = [[0] * N for _ in range(N)]

    # Populate the transitive closure matrix
    for i in range(N):
        reachable_nodes = helper(i, -1, set())
        while reachable_nodes:
            output[i][reachable_nodes.pop()] = 1

    return output