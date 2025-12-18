"""
QUESTION:
Find the cheapest price from `src` to `dst` with up to `k` stops and within `T` time in a graph with `n` cities connected by flights, each with a price `w` and time `t`. The `src` and `dst` are given, and the graph is represented by a list of flights, where each flight is a list `[u, v, w, t]`, indicating a flight from city `u` to city `v` with price `w` and time `t`.

The function should be named `findCheapestPrice`, and it should take the following parameters: `n`, `flights`, `src`, `dst`, `k`, and `T`. The function should return the cheapest price if a route exists, or -1 otherwise.

Constraints:
- 1 ≤ n ≤ 100
- 0 ≤ k ≤ n - 1
- 1 ≤ T ≤ n * 100
- 1 ≤ w ≤ 10000
- 1 ≤ t ≤ 100
"""

import heapq

def findCheapestPrice(n, flights, src, dst, k, T):
    graph = [[] for _ in range(n)]
    for u, v, w, t in flights:
        graph[u].append((v, w, t))

    dp = [[float('inf')] * (T + 1) for _ in range(k + 2)]
    dp[0][0] = 0

    pq = [(0, 0, src)]
    while pq:
        price, time, city = heapq.heappop(pq)
        if city == dst:
            return price
        if time > T:
            continue
        for neighbor, w, t in graph[city]:
            new_price, new_time, stops = price + w, time + t, 1
            if new_time <= T and new_price < dp[stops + 1][new_time]:
                dp[stops + 1][new_time] = new_price
                heapq.heappush(pq, (new_price, new_time, neighbor))
                if stops < k:
                    heapq.heappush(pq, (new_price, new_time, neighbor))

    return -1