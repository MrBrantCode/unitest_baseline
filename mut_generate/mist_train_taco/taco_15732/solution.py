"""
QUESTION:
There are N camels numbered 1 through N.
The weight of Camel i is w_i.
You will arrange the camels in a line and make them cross a bridge consisting of M parts.
Before they cross the bridge, you can choose their order in the line - it does not have to be Camel 1, 2, \ldots, N from front to back - and specify the distance between each adjacent pair of camels to be any non-negative real number.
The camels will keep the specified distances between them while crossing the bridge.
The i-th part of the bridge has length l_i and weight capacity v_i.
If the sum of the weights of camels inside a part (excluding the endpoints) exceeds v_i, the bridge will collapse.
Determine whether it is possible to make the camels cross the bridge without it collapsing. If it is possible, find the minimum possible distance between the first and last camels in the line in such a case.
It can be proved that the answer is always an integer, so print an integer.

-----Constraints-----
 - All values in input are integers.
 - 2 \leq N \leq 8
 - 1 \leq M \leq 10^5
 - 1 \leq w_i,l_i,v_i \leq 10^8

-----Input-----
Input is given from Standard Input in the following format:
N M
w_1 w_2 \cdots w_N
l_1 v_1
\vdots
l_M v_M

-----Output-----
If the bridge will unavoidably collapse when the camels cross the bridge, print -1.
Otherwise, print the minimum possible distance between the first and last camels in the line when the camels cross the bridge without it collapsing.

-----Sample Input-----
3 2
1 4 2
10 4
2 6

-----Sample Output-----
10

 - It is possible to make the camels cross the bridge without it collapsing by, for example, arranging them in the order 1, 3, 2 from front to back, and setting the distances between them to be 0, 10.
 - For Part 1 of the bridge, there are moments when only Camel 1 and 3 are inside the part and moments when only Camel 2 is inside the part. In both cases, the sum of the weights of camels does not exceed 4 - the weight capacity of Part 1 - so there is no collapse.
 - For Part 2 of the bridge, there are moments when only Camel 1 and 3 are inside the part and moments when only Camel 2 is inside the part. In both cases, the sum of the weights of camels does not exceed 6 - the weight capacity of Part 2 - so there is no collapse.
 - Note that the distance between two camels may be 0 and that camels on endpoints of a part are not considered to be inside the part.
"""

from itertools import permutations, accumulate
import heapq
import bisect
from operator import itemgetter

def min_distance_to_cross_bridge(N, M, weights, bridge_parts):
    def dijkstra(start, edge):
        n = len(edge)
        dist = [float('inf')] * n
        dist[start] = 0
        que = [(0, start)]
        while que:
            (d, v) = heapq.heappop(que)
            if dist[v] < d:
                continue
            for (nv, nd) in edge[v]:
                if dist[nv] > d + nd:
                    dist[nv] = d + nd
                    heapq.heappush(que, (dist[nv], nv))
        return dist

    # Sort bridge parts by weight capacity
    bridge_parts.sort(key=itemgetter(1))
    L, V = zip(*bridge_parts)

    # Check if any camel's weight exceeds the capacity of any part of the bridge
    w_max = max(weights)
    for v in V:
        if w_max > v:
            return -1

    # Precompute the maximum length of a part that can support the weight
    P = [0]
    for l, v in bridge_parts:
        if P[-1] < l:
            P.append(l)
        else:
            P.append(P[-1])

    def f(K):
        S = list(accumulate(weights[k] for k in K))
        edge = [[] for _ in range(N)]
        for i in range(N - 1):
            edge[i + 1].append((i, 0))
        for i in range(N - 1):
            for j in range(i + 1, N):
                if i == 0:
                    t = S[j]
                else:
                    t = S[j] - S[i - 1]
                p = P[bisect.bisect_left(V, t)]
                edge[j].append((i, -p))
        return -dijkstra(N - 1, edge)[0]

    ans = float('inf')
    for K in permutations(range(N)):
        ans = min(ans, f(K))

    return ans