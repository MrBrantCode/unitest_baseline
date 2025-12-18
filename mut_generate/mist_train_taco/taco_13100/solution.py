"""
QUESTION:
Read problem statements in [Russian], [Bengali], and [Mandarin Chinese] as well.

You are given an undirected graph with $N$ nodes (numbered $1$ through $N$) and $M$ edges. Each edge connects two distinct nodes. However, there may be multiple edges connecting the same pairs of nodes, and they are considered to be distinct edges. A lowercase English letter is written in each node.

You are also given a string $S$ with length $L$. A *beautiful path* is a sequence of $L-1$ edges such that there is a sequence of $L$ nodes with the following properties:
for each valid $i$, the $i$-th edge connects the $i$-th and $(i+1)$-th of these nodes
for each valid $i$, the $i$-th character of $S$ is written in the $i$-th of these nodes

There are no other restrictions — a path may visit nodes or edges any number of times in any order.

Determine the number of beautiful paths in the graph. Since the answer can be very large, compute it modulo $10^{9}+7$.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains three space-separated integers $N$, $M$ and $L$.
The second line contains a single string $S$ with length $L$.
The third line contains a single string with length $N$. For each valid $i$, the $i$-th character of the string is the letter written in the $i$-th node.
Two lines follow. The first line contains $M$ integers $u_{1},\ldots,u_{m}$. The second lines contains $M$ integers, $v_{1},\ldots,v_{m}$. This denotes that there is an edge connecting nodes $u_{i}$ and to $v_{i}$. These edges are distinct, even though they may connect the same pair of nodes.

------  Output ------
For each test case, print a single line containing one integer — the number of beautiful paths modulo $10^{9}+7$.

------  Constraints ------
$1 ≤ T ≤ 200$
$2 ≤ N ≤ 10^{3}$
$1 ≤ M ≤ 10^{3}$
$2 ≤ L ≤ 20$
$S$ contains only lowercase English letters
$1 ≤ u, v ≤ N$
$u \neq v$

------  Subtasks ------
Subtask #1 (100 points): original constraints

----- Sample Input 1 ------ 
2

4 4 3

aac

aaca

1 2 2 1

2 3 4 2

2 1 2

aa

aa

1

2
----- Sample Output 1 ------ 
3

1
----- explanation 1 ------ 
Example case 1: The three beautiful paths (sequences of edges) are:
- $(1,2)$, passing through nodes $(1,2,3)$ in this order
- $(4,2)$, also passing through nodes $(1,2,3)$
- $(3,2)$, passing through nodes $(4,2,3)$

Example case 2: There is only one beautiful path, which contains only edge $1$. Note that for this path (sequence of edges), there are two valid sequences of nodes: $(1,2)$ and $(2,1)$.
"""

def count_beautiful_paths(N, M, L, S, vertex, U, V):
    MOD = 10**9 + 7
    counts = [0] * N
    G = [[[] for _ in range(26)] for _ in range(N)]
    orda = ord('a')
    extras_ = [{} for _ in range(26)]
    
    # Adjust U and V to be zero-indexed
    U = [u - 1 for u in U]
    V = [v - 1 for v in V]
    
    # Build the graph
    for i in range(M):
        u, v = U[i], V[i]
        G[u][ord(vertex[v]) - orda].append(v)
        G[v][ord(vertex[u]) - orda].append(u)
        if vertex[u] == vertex[v]:
            key = (min(u, v), max(u, v))
            extras_[ord(vertex[u]) - orda][key] = extras_[ord(vertex[u]) - orda].get(key, 0) + 1
    
    # Initialize counts for the first character in S
    for i, v in enumerate(vertex):
        if v == S[0]:
            counts[i] += 1
    
    # Calculate counts for each subsequent character in S
    for i in range(1, L):
        targ = ord(S[i]) - orda
        new_counts = [0] * N
        for j in range(N):
            for x in G[j][targ]:
                new_counts[x] += counts[j]
                new_counts[x] %= MOD
        counts = list(new_counts)
    
    # Sum up the counts to get the total number of beautiful paths
    ans = sum(counts) % MOD
    
    # Adjust for paths where all characters in S are the same
    if len(set(S)) == 1:
        for key, val in extras_[ord(S[0]) - orda].items():
            ans -= pow(val, L - 1, MOD)
            ans %= MOD
    
    return ans