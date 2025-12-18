"""
QUESTION:
Given the lists `quality` and `wage` representing the quality and minimum wage expectation of each worker, and an integer `k` representing the number of workers to be hired, write a function `mincostToHireWorkers(quality, wage, k)` to find the minimum total wage cost to form a group of exactly `k` workers, where the wage of each worker is in the ratio of their quality compared to other workers in the group.

The function should take the following inputs:
- `quality`: a list of integers representing the quality of each worker, where `1 <= len(quality) <= 10^4` and `0 < quality[i] <= 10^5`.
- `wage`: a list of integers representing the minimum wage expectation for each worker, where `len(wage) = len(quality)` and `0 < wage[i] <= 10^5`.
- `k`: an integer representing the number of workers to be hired, where `1 <= k <= len(quality)`.

The function should return the minimum total wage cost to form a group of exactly `k` workers.
"""

from heapq import heappush, heappop
from typing import List

def mincostToHireWorkers(quality: List[int], wage: List[int], k: int) -> float:
    n = len(quality)
    workers = sorted((wage[i] / quality[i], quality[i]) for i in range(n))
    ans = float('inf')
    heap = []
    sumq = 0

    for ratio, q in workers:
        heappush(heap, -q)
        sumq += q

        if len(heap) > k:
            sumq += heappop(heap)

        if len(heap) == k:
            ans = min(ans, ratio * sumq)

    return ans