"""
QUESTION:
A tree is an undirected connected graph without cycles.

You are given a tree of n vertices. Find the number of ways to choose exactly k vertices in this tree (i. e. a k-element subset of vertices) so that all pairwise distances between the selected vertices are equal (in other words, there exists an integer c such that for all u, v (u ≠ v, u, v are in selected vertices) d_{u,v}=c, where d_{u,v} is the distance from u to v).

Since the answer may be very large, you need to output it modulo 10^9 + 7.

Input

The first line contains one integer t (1 ≤ t ≤ 10) — the number of test cases. Then t test cases follow.

Each test case is preceded by an empty line.

Each test case consists of several lines. The first line of the test case contains two integers n and k (2 ≤ k ≤ n ≤ 100) — the number of vertices in the tree and the number of vertices to be selected, respectively. Then n - 1 lines follow, each of them contains two integers u and v (1 ≤ u, v ≤ n, u ≠ v) which describe a pair of vertices connected by an edge. It is guaranteed that the given graph is a tree and has no loops or multiple edges.

Output

For each test case output in a separate line a single integer — the number of ways to select exactly k vertices so that for all pairs of selected vertices the distances between the vertices in the pairs are equal, modulo 10^9 + 7 (in other words, print the remainder when divided by 1000000007).

Example

Input


3

4 2
1 2
2 3
2 4

3 3
1 2
2 3

5 3
1 2
2 3
2 4
4 5


Output


6
0
1
"""

def count_k_vertex_subsets(n, k, edges):
    MOD = 10**9 + 7
    
    # Create adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
    
    if k == 2:
        return (n * (n - 1) // 2) % MOD
    
    central_nodes = []
    for node in range(n):
        if len(adj[node]) >= k:
            central_nodes.append(node)
    
    ans = 0
    for cn in central_nodes:
        visited = [False] * n
        visited[cn] = True
        groups = []
        for nex in adj[cn]:
            visited[nex] = True
            groups.append([nex])
        
        while len(groups) >= k:
            N = len(groups)
            M = k
            dp = [[0 for _ in range(M + 1)] for _ in range(N)]
            for i in range(N):
                dp[i][0] = 1
            dp[0][1] = len(groups[0])
            for i in range(1, N):
                for j in range(1, M + 1):
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] * len(groups[i])
                    dp[i][j] %= MOD
            ans += dp[N - 1][M]
            ans %= MOD
            
            groups2 = []
            for gp in groups:
                temp = []
                for node in gp:
                    for nex in adj[node]:
                        if visited[nex]:
                            continue
                        visited[nex] = True
                        temp.append(nex)
                if len(temp) > 0:
                    groups2.append(temp)
            groups = groups2
    
    return ans