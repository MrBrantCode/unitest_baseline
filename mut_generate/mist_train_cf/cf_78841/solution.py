"""
QUESTION:
Create a function called `maxPerformance` that takes five parameters: `n`, `speed`, `efficiency`, `cost`, and `k`, `B`. `n` is the number of engineers, `speed`, `efficiency`, and `cost` are arrays representing the speed, efficiency, and cost of each engineer respectively, `k` is the maximum number of engineers in a team, and `B` is the budget for the team. Return the maximum performance of a team composed of at most `k` engineers, under a budget `B`, modulo 10^9 + 7. The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.
"""

import heapq

def maxPerformance(n, speed, efficiency, cost, k, B):
    engineers = sorted(zip(cost, speed, efficiency), key=lambda x: x[2], reverse=True)
    
    max_result, total_speeds, heap = 0, 0, []
    for c, s, e in engineers:
        if len(heap) < k:
            total_speeds += s
            heapq.heappush(heap, s)
        elif heap and heap[0] < s and c + sum(heap) - heap[0] <= B:
            total_speeds += s - heapq.heappushpop(heap, s)
        if c + sum(heap) <= B:
            max_result = max(max_result, total_speeds * e)
    
    return max_result % (10**9 + 7)