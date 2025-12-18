"""
QUESTION:
Appleman has a tree with n vertices. Some of the vertices (at least one) are colored black and other vertices are colored white.

Consider a set consisting of k (0 ≤ k < n) edges of Appleman's tree. If Appleman deletes these edges from the tree, then it will split into (k + 1) parts. Note, that each part will be a tree with colored vertices.

Now Appleman wonders, what is the number of sets splitting the tree in such a way that each resulting part will have exactly one black vertex? Find this number modulo 1000000007 (109 + 7).

Input

The first line contains an integer n (2 ≤ n ≤ 105) — the number of tree vertices. 

The second line contains the description of the tree: n - 1 integers p0, p1, ..., pn - 2 (0 ≤ pi ≤ i). Where pi means that there is an edge connecting vertex (i + 1) of the tree and vertex pi. Consider tree vertices are numbered from 0 to n - 1.

The third line contains the description of the colors of the vertices: n integers x0, x1, ..., xn - 1 (xi is either 0 or 1). If xi is equal to 1, vertex i is colored black. Otherwise, vertex i is colored white.

Output

Output a single integer — the number of ways to split the tree modulo 1000000007 (109 + 7).

Examples

Input

3
0 0
0 1 1


Output

2


Input

6
0 1 1 0 4
1 1 0 0 1 0


Output

1


Input

10
0 1 2 1 4 4 4 0 8
0 0 0 1 0 1 1 0 0 1


Output

27
"""

def count_valid_splits(n, edges, colors):
    MOD = 1000000007
    
    # Build the graph
    graph = [[] for _ in range(n)]
    for (a, b) in enumerate(edges):
        graph[a + 1].append(b)
        graph[b].append(a + 1)
    
    # Initialize DP and visited arrays
    dp = [[0] * 2 for _ in range(n)]
    visited = [0] * n
    
    # DFS stack
    stack = [0]
    
    while stack:
        v = stack[-1]
        visited[v] = -1
        cn = 0
        for u in graph[v]:
            if visited[u] != 0:
                continue
            else:
                cn += 1
                stack.append(u)
        if not cn:
            dp[v][0] = 1
            dp[v][1] = 0
            for u in graph[v]:
                if visited[u] == -1:
                    continue
                dp[v][1] *= dp[u][0]
                dp[v][1] += dp[v][0] * dp[u][1]
                dp[v][0] *= dp[u][0]
                dp[v][1] %= MOD
                dp[v][0] %= MOD
            if colors[v] == 1:
                dp[v][1] = dp[v][0]
            else:
                dp[v][0] += dp[v][1]
                dp[v][0] %= MOD
            visited[v] = 1
            stack.pop()
    
    return dp[0][1]