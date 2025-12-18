"""
QUESTION:
D - Medical Inspection

Problem Statement

The government has declared a state of emergency due to the MOFU syndrome epidemic in your country. Persons in the country suffer from MOFU syndrome and cannot get out of bed in the morning. You are a programmer working for the Department of Health. You have to take prompt measures.

The country consists of n islands numbered from 1 to n and there are ocean liners between some pair of islands. The Department of Health decided to establish the quarantine stations in some islands and restrict an infected person's moves to prevent the expansion of the epidemic. To carry out this plan, there must not be any liner such that there is no quarantine station in both the source and the destination of the liner. The problem is the department can build at most K quarantine stations due to the lack of budget.

Your task is to calculate whether this objective is possible or not. And if it is possible, you must calculate the minimum required number of quarantine stations.

Input

The test case starts with a line containing three integers N (2 \leq N \leq 3{,}000), M (1 \leq M \leq 30{,}000) and K (1 \leq K \leq 32). Each line in the next M lines contains two integers a_i (1 \leq a_i \leq N) and b_i (1 \leq b_i \leq N). This represents i-th ocean liner connects island a_i and b_i. You may assume a_i \neq b_i for all i, and there are at most one ocean liner between all the pairs of islands.

Output

If there is no way to build quarantine stations that satisfies the objective, print "Impossible" (without quotes). Otherwise, print the minimum required number of quarantine stations.

Sample Input 1


3 3 2
1 2
2 3
3 1


Output for the Sample Input 1


2


Sample Input 2


3 3 1
1 2
2 3
3 1


Output for the Sample Input 2


Impossible


Sample Input 3


7 6 5
1 3
2 4
3 5
4 6
5 7
6 2


Output for the Sample Input 3


4


Sample Input 4


10 10 10
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5


Output for the Sample Input 4


4






Example

Input

3 3 2
1 2
2 3
3 1


Output

2
"""

from collections import deque
import sys

def minimum_quarantine_stations(N, M, K, ocean_liners):
    G = [[] for _ in range(N)]
    for (a, b) in ocean_liners:
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    
    D = list(map(len, G))
    I = list(range(N))
    I.sort(key=D.__getitem__, reverse=True)
    
    INF = 10 ** 9

    def dfs(i, state, c):
        if i == N:
            return c
        v = I[i]
        res = INF
        e1 = []
        for w in G[v]:
            if state[w]:
                continue
            e1.append(w)
        if c + len(e1) <= K:
            for w in e1:
                state[w] = 1
            k = i + 1
            while k < N and state[I[k]]:
                k += 1
            res = min(res, dfs(k, state, c + len(e1)))
            for w in e1:
                state[w] = 0
        if len(e1) > 1 and c + 1 <= K:
            state[v] = 1
            k = i
            while k < N and state[I[k]]:
                k += 1
            res = min(res, dfs(k, state, c + 1))
            state[v] = 0
        return res
    
    res = dfs(0, [0] * N, 0)
    if res < INF:
        return res
    else:
        return "Impossible"