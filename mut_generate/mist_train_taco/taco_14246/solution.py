"""
QUESTION:
Example

Input

5
1 2
1 3
1 4
1 5


Output

6
"""

from collections import deque, defaultdict

def calculate_tree_combinations(N, edges):
    G = [[] for _ in range(N)]
    for (a, b) in edges:
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    
    H = [-1] * N
    MOD = 10 ** 9 + 9
    X1 = [0] * N
    v1 = 13
    X2 = [0] * N
    v2 = 17
    U = [0] * N
    que = deque([0])
    U[0] = 1
    D = [0]
    
    while que:
        v = que.popleft()
        for w in G[v]:
            if U[w]:
                continue
            U[w] = 1
            que.append(w)
            D.append(w)
    
    M = defaultdict(int)
    for v in reversed(D):
        h = 0
        su1 = su2 = 0
        for w in G[v]:
            if H[w] == -1:
                continue
            h = max(h, H[w])
            su1 += X1[w]
            su2 += X2[w]
        H[v] = k = h + 1
        X1[v] = w1 = (su1 * v1 + 1) % MOD
        X2[v] = w2 = (su2 * v2 + 1) % MOD
        M[k, w1, w2] += 1
    
    ans = 0
    for v in M.values():
        ans += v * (v - 1) // 2
    
    return ans