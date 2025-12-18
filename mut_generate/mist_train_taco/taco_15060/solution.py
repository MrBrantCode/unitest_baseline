"""
QUESTION:
You are given a weighted graph with $N$ nodes and $M$ edges. Some of the nodes are marked as special nodes. Your task is to find the shortest pairwise distance between any two different special nodes.

-----Input-----
- The first line of the input contains three space-separated integers $N$, $M$ and $K$ denoting the number of nodes, the number of edges, and the number of special nodes. 
- The next line contains $K$ space-separated distinct integers $A_{1}$, $A_{2}$, $\ldots$, $A_{K}$, denoting the special nodes.
- The next $M$ lines each contain three space-separated integers - $X$, $Y$, $Z$, denoting an edge connecting the nodes $X$ and $Y$, with weight $Z$.

-----Output-----
Output the shortest pairwise distance between any two different special nodes.

-----Constraints-----
- The given graph is connected.
- The given graph doesn't contain self loops and multiple edges.
- $1 \leq A_{i} \leq N$
- $1 \leq Z_{j} \leq 10^{4}$
- $1 \leq X_{j}, Y_{j} \leq N$

-----Subtasks-----
Subtask #1 (20 points): 
- $2 \leq N \leq 300$
- $N-1 \leq M \leq \frac{N \cdot (N-1)}{2}$
- $2 \leq K \leq N$
Subtask #2 (25 points):
- $2 \leq N \leq 10^5$
- $N-1 \leq M \leq 10^5$
- $2 \leq K \leq 10$
Subtask #3 (55 points):
- $2 \leq N \leq 10^5$
- $N-1 \leq M \leq 3 \cdot 10^5$
- $2 \leq K \leq 10^4$

-----Example Input-----
5 5 3
1 3 5
1 2 3
2 3 4
3 4 1
4 5 8
1 5 19

-----Example Output-----
7

-----Explanation-----
Nodes $1$, $3$, and $5$ are special nodes. Shortest distance between nodes $1$ and $3$ is $7$, and that between nodes $3$ and $5$ is $9$. Shortest distance between nodes $1$ and $5$ is $16$. Minimum of these distances is $7$. Hence answer is $7$.
"""

def find_shortest_special_node_distance(N, M, K, special_nodes, edges):
    # Initialize the distance matrix
    dp = [[float('inf')] * N for _ in range(N)]
    
    # Set the distance from a node to itself as 0
    for i in range(N):
        dp[i][i] = 0
    
    # Fill the distance matrix with edge weights
    for x, y, z in edges:
        dp[x - 1][y - 1] = z
        dp[y - 1][x - 1] = z
    
    # Floyd-Warshall algorithm to find all pairs shortest paths
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
    
    # Find the shortest distance between any two special nodes
    shortest_distance = float('inf')
    for i in range(K):
        for j in range(i + 1, K):
            shortest_distance = min(shortest_distance, dp[special_nodes[i] - 1][special_nodes[j] - 1])
    
    return shortest_distance