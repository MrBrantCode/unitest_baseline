"""
QUESTION:
Write a function `mincostToHireWorkers(quality, wage, K)` that takes in three inputs: 
- `quality`, an array of integers representing the quality of work for each worker
- `wage`, an array of integers representing the minimum wage expectation for each worker
- `K`, an integer representing the number of workers to be hired

The function should return the smallest possible total payment required to hire exactly `K` workers, where each worker is paid in proportion to their quality, and their payment is at least equal to their minimum wage expectation.

The inputs are subject to the following constraints: 
- `1 <= K <= N <= 10000`, where `N = quality.length = wage.length`
- `1 <= quality[i] <= 10000`
- `1 <= wage[i] <= 10000`
"""

import heapq

def mincostToHireWorkers(quality, wage, K):
    workers = sorted([float(w) / q, q] for w, q in zip(wage, quality))
    res = float('inf')
    qsum = 0
    queue = []
    
    for r, q in workers:
        heapq.heappush(queue, -q)
        qsum += q
        if len(queue) > K: 
            qsum += heapq.heappop(queue)
        if len(queue) == K: 
            res = min(res, qsum * r)
    
    return res