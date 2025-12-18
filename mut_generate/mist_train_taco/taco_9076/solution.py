"""
QUESTION:
Problem

There are N islands and M bridges. Numbers from 1 to N are assigned to each of the N islands. Numbers from 1 to M are also assigned to each of the M bridges.

Gaccho is currently on the first island (at time 0). Gaccho can move from the ai-th island to the bi-th island in one direction by using the i-th bridge.

However, at time 0, all the bridges were full of tide and sank into the sea. The i-th bridge will be able to cross the tide at time ci. And soon after the time ci, the tide rises again and the i-th bridge sinks again. When it sinks again, I don't know when the tide will pull and cross. So, Gaccho decided to think that such a bridge would never be crossed.

Gaccho wants to see the scenery of the 1st to N-1st islands for as long as possible, but since he is staying at the Nth island, he finally arrives at the Nth island. There must be. Also, because he keeps his parents waiting on the boat, Gacho must leave by boat and go home as soon as he arrives at the Nth island.

The time it takes for Gaccho to cross the bridge and travel around the island is very short, so you can assume it is 0. Find the maximum amount of time Gaccho can be on any of the 1st to N-1 islands. However, if you can't move to the Nth island no matter how you move, output -1 instead.

Constraints

* 2 ≤ N ≤ 105
* 1 ≤ M ≤ 2 × 105
* 1 ≤ ai <N
* 1 ≤ bi ≤ N
* 1 ≤ ci ≤ 109
* ai ≠ bi

Input

The input is given in the following format.


N M
a1 b1 c1
a2 b2 c2
...
aM bM cM


On the first line, two integers N and M are given, separated by blanks.
Three integers ai, bi, ci are given in each line i from the second line to the M + 1 line, separated by blanks.

Output

If Gaccho can move to the Nth island, it will output the maximum amount of time that Gaccho can be on any of the 1st to N-1th islands. If it cannot move to the Nth island, it prints -1 instead.

Examples

Input

3 2
1 2 10
2 3 20


Output

20


Input

4 4
1 2 27
1 3 37
2 3 47
3 1 57


Output

-1


Input

3 3
1 2 13
2 3 17
2 3 15


Output

17


Input

3 2
1 2 20
2 3 10


Output

-1


Input

3 2
1 2 10
2 3 10


Output

10
"""

import heapq

INF = 2147483647

def dijkstra(V, to, start):
    dist = [INF] * V
    Q = []
    dist[start] = 0
    heapq.heappush(Q, (0, start))
    while Q:
        (t, s) = heapq.heappop(Q)
        if dist[s] < t:
            continue
        for (e, cost) in to[s]:
            if t <= cost and cost < dist[e]:
                dist[e] = cost
                heapq.heappush(Q, (cost, e))
    return dist

def find_max_stay_time(N, M, bridges):
    n1 = N - 1
    last = []
    to = [[] for _ in range(N)]
    
    for (a, b, c) in bridges:
        a -= 1
        b -= 1
        to[a].append((b, c))
        if b == n1:
            last.append((a, c))
    
    dist = dijkstra(N, to, 0)
    
    if dist[n1] >= INF:
        return -1
    
    last.sort(key=lambda x: -x[1])
    for (a, c) in last:
        if dist[a] <= c:
            return c
    
    return -1