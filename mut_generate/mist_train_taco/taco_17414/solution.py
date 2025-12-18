"""
QUESTION:
There is a directed graph G with N vertices and M edges. The vertices are numbered 1, 2, \ldots, N, and for each i (1 \leq i \leq M), the i-th directed edge goes from Vertex x_i to y_i. G does not contain directed cycles.

Find the length of the longest directed path in G. Here, the length of a directed path is the number of edges in it.

Constraints

* All values in input are integers.
* 2 \leq N \leq 10^5
* 1 \leq M \leq 10^5
* 1 \leq x_i, y_i \leq N
* All pairs (x_i, y_i) are distinct.
* G does not contain directed cycles.

Input

Input is given from Standard Input in the following format:


N M
x_1 y_1
x_2 y_2
:
x_M y_M


Output

Print the length of the longest directed path in G.

Examples

Input

4 5
1 2
1 3
3 2
2 4
3 4


Output

3


Input

6 3
2 3
4 5
5 6


Output

2


Input

5 8
5 3
2 3
2 4
5 2
5 1
1 4
4 3
1 3


Output

3
"""

def longest_directed_path(n, m, edges):
    # Create the adjacency list for the graph
    g = [[] for _ in range(n)]
    for x, y in edges:
        g[x - 1].append(y - 1)
    
    # Initialize the dp array
    dp = [-1] * n
    
    # Recursive function to calculate the longest path from a vertex
    def rec(v):
        if dp[v] != -1:
            return dp[v]
        else:
            res = 0
            for u in g[v]:
                res = max(res, rec(u) + 1)
            dp[v] = res
            return dp[v]
    
    # Calculate the longest path for each vertex
    for i in range(n):
        rec(i)
    
    # Return the maximum value in the dp array
    return max(dp)