"""
QUESTION:
An undirected graph is given. Each edge of the graph disappears with a constant probability. Calculate the probability with which the remained graph is connected.



Input

The first line contains three integers N (1 \leq N \leq 14), M (0 \leq M \leq 100) and P (0 \leq P \leq 100), separated by a single space. N is the number of the vertices and M is the number of the edges. P is the probability represented by a percentage.

The following M lines describe the edges. Each line contains two integers v_i and u_i (1 \leq u_i, v_i \leq N). (u_i, v_i) indicates the edge that connects the two vertices u_i and v_i.

Output

Output a line containing the probability with which the remained graph is connected. Your program may output an arbitrary number of digits after the decimal point. However, the absolute error should be 10^{-9} or less.

Examples

Input

3 3 50
1 2
2 3
3 1


Output

0.500000000000


Input

3 3 10
1 2
2 3
3 1


Output

0.972000000000


Input

4 5 50
1 2
2 3
3 4
4 1
1 3


Output

0.437500000000
"""

from collections import deque

def calculate_connected_graph_probability(N, M, P, edges):
    G = [[] for _ in range(N)]
    for u, v in edges:
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
    
    N1 = 1 << N
    bc = [0] * N1
    for i in range(1, N1):
        bc[i] = bc[i ^ (i & -i)] + 1
    
    ec = [0] * N1
    for state in range(1, N1):
        c = 0
        for v in range(N):
            if state & (1 << v) == 0:
                continue
            for w in G[v]:
                if state & (1 << w) == 0:
                    continue
                c += 1
        ec[state] = c >> 1
    
    N0 = 1 << (N - 1)
    dp = [0] * N1
    dp[1] = 1
    
    for s0 in range(1, N0):
        state0 = (s0 << 1) | 1
        state1 = state0 - 1 & state0
        v = 0
        while state1:
            if state1 & 1:
                k = ec[state0] - ec[state1] - ec[state0 ^ state1]
                v += dp[state1] * ((P / 100) ** k)
            state1 = state1 - 1 & state0
        dp[state0] = 1 - v
    
    return dp[N1 - 1]