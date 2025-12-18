"""
QUESTION:
Bankopolis is an incredible city in which all the n crossroads are located on a straight line and numbered from 1 to n along it. On each crossroad there is a bank office.

The crossroads are connected with m oriented bicycle lanes (the i-th lane goes from crossroad ui to crossroad vi), the difficulty of each of the lanes is known.

Oleg the bank client wants to gift happiness and joy to the bank employees. He wants to visit exactly k offices, in each of them he wants to gift presents to the employees.

The problem is that Oleg don't want to see the reaction on his gifts, so he can't use a bicycle lane which passes near the office in which he has already presented his gifts (formally, the i-th lane passes near the office on the x-th crossroad if and only if min(ui, vi) < x < max(ui, vi))). Of course, in each of the offices Oleg can present gifts exactly once. Oleg is going to use exactly k - 1 bicycle lane to move between offices. Oleg can start his path from any office and finish it in any office.

Oleg wants to choose such a path among possible ones that the total difficulty of the lanes he will use is minimum possible. Find this minimum possible total difficulty.

Input

The first line contains two integers n and k (1 ≤ n, k ≤ 80) — the number of crossroads (and offices) and the number of offices Oleg wants to visit.

The second line contains single integer m (0 ≤ m ≤ 2000) — the number of bicycle lanes in Bankopolis.

The next m lines contain information about the lanes.

The i-th of these lines contains three integers ui, vi and ci (1 ≤ ui, vi ≤ n, 1 ≤ ci ≤ 1000), denoting the crossroads connected by the i-th road and its difficulty.

Output

In the only line print the minimum possible total difficulty of the lanes in a valid path, or -1 if there are no valid paths.

Examples

Input

7 4
4
1 6 2
6 2 2
2 4 2
2 7 1


Output

6


Input

4 3
4
2 1 2
1 3 2
3 4 2
4 1 1


Output

3

Note

In the first example Oleg visiting banks by path 1 → 6 → 2 → 4.

Path 1 → 6 → 2 → 7 with smaller difficulity is incorrect because crossroad 2 → 7 passes near already visited office on the crossroad 6.

In the second example Oleg can visit banks by path 4 → 1 → 3.
"""

import sys
from functools import lru_cache

def find_minimum_difficulty(n, k, m, lanes):
    INF = float('inf')
    
    if k < 2:
        return 0
    
    edge = [[] for _ in range(n + 1)]
    cost = {}
    
    for (u, v, c) in lanes:
        if (u, v) in cost:
            cost[u, v] = min(cost[u, v], c)
        else:
            edge[u].append(v)
            cost[u, v] = c
    
    @lru_cache(maxsize=None)
    def recur(v, s, e, k):
        if k == 0:
            return 0
        elif k > e - s + 1:
            return INF
        ret = INF
        for nv in edge[v]:
            if not s <= nv <= e:
                continue
            tmp = [0] * 2
            if v < nv:
                tmp[0] = recur(nv, max(s, v + 1), nv - 1, k - 1)
                tmp[1] = recur(nv, nv + 1, e, k - 1)
            else:
                tmp[0] = recur(nv, s, nv - 1, k - 1)
                tmp[1] = recur(nv, nv + 1, min(v - 1, e), k - 1)
            if min(tmp) + cost[v, nv] < ret:
                ret = min(tmp) + cost[v, nv]
        return ret
    
    ans = INF
    for v in range(1, n + 1):
        for nv in edge[v]:
            tmp = [INF] * 2
            if v < nv:
                tmp[0] = recur(nv, nv + 1, n, k - 2)
                tmp[1] = recur(nv, v + 1, nv - 1, k - 2)
            else:
                tmp[0] = recur(nv, 1, nv - 1, k - 2)
                tmp[1] = recur(nv, nv + 1, v - 1, k - 2)
            if min(tmp) + cost[v, nv] < ans:
                ans = min(tmp) + cost[v, nv]
    
    return ans if ans != INF else -1