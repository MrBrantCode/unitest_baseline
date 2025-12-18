"""
QUESTION:
Given a wooden stick of length `n` units and an integer array `cuts` where `cuts[i]` denotes a position to perform a cut, return the minimum total cost of the cuts. The cost of one cut is the length of the stick to be cut, and the total cost is the sum of costs of all cuts. A cut can only be made if the resulting smaller stick has a length that is a prime number. If it is not possible to make any cuts that satisfy this condition, return -1. 

Function name: minCost(n, cuts)
"""

import heapq

def minCost(n, cuts):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    cuts.append(0)
    cuts.append(n)
    cuts.sort()
    pq = []
    for i in range(1, len(cuts)):
        if not is_prime(cuts[i] - cuts[i-1]):
            return -1
        heapq.heappush(pq, cuts[i] - cuts[i-1])
    res = 0
    while len(pq) > 1:
        x = heapq.heappop(pq)
        y = heapq.heappop(pq)
        res += x + y
        heapq.heappush(pq, x + y)
    return res