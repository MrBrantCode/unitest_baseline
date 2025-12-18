"""
QUESTION:
Goa'uld Apophis captured Jack O'Neill's team again! Jack himself was able to escape, but by that time Apophis's ship had already jumped to hyperspace. But Jack knows on what planet will Apophis land. In order to save his friends, Jack must repeatedly go through stargates to get to this planet.

Overall the galaxy has n planets, indexed with numbers from 1 to n. Jack is on the planet with index 1, and Apophis will land on the planet with index n. Jack can move between some pairs of planets through stargates (he can move in both directions); the transfer takes a positive, and, perhaps, for different pairs of planets unequal number of seconds. Jack begins his journey at time 0.

It can be that other travellers are arriving to the planet where Jack is currently located. In this case, Jack has to wait for exactly 1 second before he can use the stargate. That is, if at time t another traveller arrives to the planet, Jack can only pass through the stargate at time t + 1, unless there are more travellers arriving at time t + 1 to the same planet.

Knowing the information about travel times between the planets, and the times when Jack would not be able to use the stargate on particular planets, determine the minimum time in which he can get to the planet with index n.

Input

The first line contains two space-separated integers: n (2 ≤ n ≤ 105), the number of planets in the galaxy, and m (0 ≤ m ≤ 105) — the number of pairs of planets between which Jack can travel using stargates. Then m lines follow, containing three integers each: the i-th line contains numbers of planets ai and bi (1 ≤ ai, bi ≤ n, ai ≠ bi), which are connected through stargates, and the integer transfer time (in seconds) ci (1 ≤ ci ≤ 104) between these planets. It is guaranteed that between any pair of planets there is at most one stargate connection.

Then n lines follow: the i-th line contains an integer ki (0 ≤ ki ≤ 105) that denotes the number of moments of time when other travellers arrive to the planet with index i. Then ki distinct space-separated integers tij (0 ≤ tij < 109) follow, sorted in ascending order. An integer tij means that at time tij (in seconds) another traveller arrives to the planet i. It is guaranteed that the sum of all ki does not exceed 105.

Output

Print a single number — the least amount of time Jack needs to get from planet 1 to planet n. If Jack can't get to planet n in any amount of time, print number -1.

Examples

Input

4 6
1 2 2
1 3 3
1 4 8
2 3 4
2 4 5
3 4 3
0
1 3
2 3 4
0


Output

7


Input

3 1
1 2 3
0
1 3
0


Output

-1

Note

In the first sample Jack has three ways to go from planet 1. If he moves to planet 4 at once, he spends 8 seconds. If he transfers to planet 3, he spends 3 seconds, but as other travellers arrive to planet 3 at time 3 and 4, he can travel to planet 4 only at time 5, thus spending 8 seconds in total. But if Jack moves to planet 2, and then — to planet 4, then he spends a total of only 2 + 5 = 7 seconds.

In the second sample one can't get from planet 1 to planet 3 by moving through stargates.
"""

from heapq import heappush, heappop, heapify
from bisect import bisect_left

def minimum_time_to_planet(n, m, connections, delays):
    # Initialize the adjacency list for the graph
    l = [[] for _ in range(n + 1)]
    for (a, b, c) in connections:
        l[a].append((c, b))
        l[b].append((c, a))
    
    # Initialize the distance array with a large number
    dist = [10000000000] * (n + 1)
    
    def helper(lst, val):
        if not lst or lst[0] > val or lst[-1] < val:
            return val
        v = bisect_left(lst, val)
        if v < len(lst) and lst[v] == val:
            l = 1
            h = len(lst) - v
            z = 20000000000
            while l < h:
                m = (l + h) // 2
                if v + m < len(lst) and val + m == lst[v + m]:
                    l = m + 1
                else:
                    h, z = m, m
            return (lst[-1] + 1 - val if z == 20000000000 else z) + val
        return val
    
    def dij_modified(delay, t):
        vis = [0] * (n + 1)
        dist[1] = t
        h = []
        heappush(h, (t, 1))
        heapify(h)
        while h:
            val = heappop(h)
            if vis[val[1]] != 0:
                continue
            vis[val[1]] = 1
            x = val[1]
            if len(delay[x - 1]) > 0 and x != n:
                dist[x] = helper(delay[x - 1], dist[x])
            for i in l[x]:
                d = i[0]
                e = i[1]
                if dist[x] + d < dist[e]:
                    dist[e] = dist[x] + d
                    heappush(h, (dist[e], e))
    
    dij_modified(delays, 0)
    
    return dist[n] if dist[n] < 10000000000 else -1