"""
QUESTION:
Write a function `eatenApples(apples, days, m)` that takes three inputs: two integer arrays `apples` and `days` of length `n`, and an integer `m`. The function should return the maximum number of apples you can eat given the constraints that you can eat at most one apple a day and you can only eat apples on `m` number of consecutive days before taking a break for a day. The apple tree grows `apples[i]` apples on the `i-th` day that will rot after `days[i]` days. The function should assume that `apples.length == n`, `days.length == n`, `1 <= n <= 2 * 10^4`, `0 <= apples[i], days[i] <= 2 * 10^4`, `days[i] = 0` if and only if `apples[i] = 0`, and `1 <= m <= n`.
"""

import heapq

def eatenApples(apples, days, m):
    pq, res, eatingDay = [], 0, 0
    for i in range(len(apples)):
        if eatingDay == m: 
            eatingDay -= 1
            if pq: heapq.heappop(pq)
        if apples[i] > 0:
            heapq.heappush(pq, (i+days[i], apples[i]))
        while pq and pq[0][0] <= i:
            heapq.heappop(pq)
        if pq:
            res += 1
            eatingDay += 1
            if pq[0][1] > 1: 
                heapq.heapreplace(pq, (pq[0][0], pq[0][1]-1))
            else: 
                heapq.heappop(pq)
    while pq:
        if eatingDay == m: 
            eatingDay -= 1
            heapq.heappop(pq)
        if pq:
            res += 1
            eatingDay += 1
            if pq[0][1] > 1: 
                heapq.heapreplace(pq, (pq[0][0], pq[0][1]-1))
            else: 
                heapq.heappop(pq)
    return res