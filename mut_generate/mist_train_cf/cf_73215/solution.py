"""
QUESTION:
Write a function named `maximumBerries` that takes two integer arrays `berries` and `days` of equal length `n` as input, where `berries[i]` is the number of berries produced on the `i-th` day and `days[i]` is the number of days the berries will be available for harvesting. The function should return the maximum number of berries that can be harvested, given that at most one berry can be harvested per day and berries that are not harvested within their available days will wither.

Constraints: `1 <= n <= 2 * 10^4` and `0 <= berries[i], days[i] <= 2 * 10^4`. `days[i] = 0` if and only if `berries[i] = 0`.
"""

import heapq

def maximumBerries(berries, days):
    heap = []
    res = j = 0
    for i in range(1, 20010):
        while j < len(berries) and j + 1 <= i:
            if days[j] >= i:
                heapq.heappush(heap, -berries[j])
            j += 1
        if heap:
            res += -heapq.heappop(heap)
    return res