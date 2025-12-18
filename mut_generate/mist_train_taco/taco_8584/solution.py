"""
QUESTION:
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well. 

Sereja has an undirected graph on N vertices. There are edges between all but M pairs of vertices.

A permutation p on the vertices of the graph is represented as p[1], p[2], … , p[N] such that for all i, p[i] is a vertex of the graph. A permutation is called connected if there is an edge between vertices p[i] and p[i+1] for all natural numbers i less than N. Sereja wants to know the number of connected permutations on the graph vertices.

------ Input ------ 

First line of input contains a single integer T, denoting the number of test cases. T tests follow. First line of each test case contains two integers, N and M. M lines follow, each containing a pair of indices of vertices, indicating that those vertices are not connected by an edge.

------ Output ------ 

For each test case, output one number — the answer for the problem modulo 10^{9}+7.

------ Constraints ------ 

$1 ≤ T ≤  10 $
$1 ≤ N ≤  10^{5}$
$0 ≤ M ≤  7 $

------ Subtasks ------ 

$Subtask #1:  1 ≤ N ≤  10  (25 points) $
$Subtask #2:  1 ≤ N ≤  100  (25 points) $
$Subtask #3:  1 ≤ N ≤  1000  (25 points) $
$Subtask #4:   original  (25 points) $

----- Sample Input 1 ------ 
2
4 3
1 2
2 3
3 4
2 1
1 2
----- Sample Output 1 ------ 
2
0
"""

from collections import defaultdict

MOD = 1000000007
MX = 100010
(fact, inv_fact) = ([1] * MX, [1] * MX)
for i in range(2, MX):
    fact[i] = fact[i - 1] * i % MOD
inv_fact[MX - 1] = 549915853
for i in range(MX - 2, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

def ncr(n, r):
    if n < r:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

def count_connected_permutations(n, m, disconnected_pairs):
    if m == 0:
        return fact[n] % MOD
    
    faulty_nodes = []
    discon = defaultdict(lambda: 0)
    
    for u, v in disconnected_pairs:
        discon[u, v] = 1
        discon[v, u] = 1
        if u not in faulty_nodes:
            faulty_nodes.append(u)
        if v not in faulty_nodes:
            faulty_nodes.append(v)
    
    k = len(faulty_nodes)
    normal_nodes = n - k
    normal_nodes_combinations = fact[normal_nodes]
    ans = 0
    dp = [[[0] * (k + 1) for _ in range(k + 1)] for _ in range(1 << k + 1)]
    
    for i in range(k):
        dp[1 << i][i][0] = 1
    
    for mask in range(1, 1 << k):
        for first_node in range(k):
            for number_tied in range(k):
                if dp[mask][first_node][number_tied] > 0:
                    for new_first in range(k):
                        if mask >> new_first & 1 == 0:
                            new_mask = mask ^ 1 << new_first
                            edge_missing = discon[faulty_nodes[first_node], faulty_nodes[new_first]]
                            dp[new_mask][new_first][number_tied + edge_missing] += dp[mask][first_node][number_tied]
                if mask == (1 << k) - 1:
                    get_ways = ncr(n - number_tied, k) * dp[mask][first_node][number_tied] * normal_nodes_combinations % MOD
                    ans = (ans + get_ways) % MOD
    
    return ans