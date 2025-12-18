"""
QUESTION:
Find the cheapest price for a flight path from a source city to a destination city with at most k stops. 

Function: `findCheapestPrice(n, flights, src, dst, k)`

- `n`: The number of cities (nodes) in the flight network.
- `flights`: A list of tuples containing the source, destination, and price of each flight.
- `src`: The source city.
- `dst`: The destination city.
- `k`: The maximum number of stops allowed.

Return the cheapest price from `src` to `dst` with at most `k` stops. If no such route exists, return -1.
"""

import collections
import heapq

def findCheapestPrice(n, flights, src, dst, k):
    graph = collections.defaultdict(list)
    for s, d, p in flights:
        graph[s].append((d, p))

    heap = [(0, src, k + 1)]
    while heap:
        price, city, stops = heapq.heappop(heap)
        if city == dst:
            return price
        if stops > 0:
            for neighbor, cost in graph[city]:
                heapq.heappush(heap, (price + cost, neighbor, stops - 1))
    return -1