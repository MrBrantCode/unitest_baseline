"""
QUESTION:
There are n cities and m edges connected by some number of flights. You are given an array flights where flights[i] = [from_{i}, to_{i}, price_{i}] indicates that there is a flight from the city from_{i} to city to_{i} with cost price_{i}.
You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
 
Note: The price from city A to B may be different From price from city B to A. 
Example 1:
Input:
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
Output:
700
Explanation:
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
Constraint:
1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= from_{i}, to_{i} < n
from_{i} != to_{i}
1 <= price_{i} <= 10^{4}
There will not be any multiple flights between the two cities.
0 <= src, dst, k < n
src != dst
"""

import queue
from typing import List

def find_cheapest_flight(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    dist = [float('inf')] * n
    adjList = {}
    for i in range(n):
        adjList[i] = []
    for flight in flights:
        u = flight[0]
        v = flight[1]
        price = flight[2]
        adjList[u].append([v, price])
    
    s = queue.Queue()
    starting_stop = 0
    starting_price = 0
    s.put([starting_stop, starting_price, src])
    
    while not s.empty():
        (stop, price, node) = s.get()
        if stop > k:
            break
        for i in adjList[node]:
            adjNode = i[0]
            curr_price = i[1]
            net_price = price + curr_price
            if net_price < dist[adjNode]:
                s.put([stop + 1, net_price, adjNode])
                dist[adjNode] = net_price
    
    if dist[dst] == float('inf'):
        return -1
    return dist[dst]