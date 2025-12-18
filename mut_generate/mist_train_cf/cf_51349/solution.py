"""
QUESTION:
Implement the `lastStoneWeight` function, which takes a list of stone weights as input. In each round, select the two heaviest stones and collide them. If the weights are equal, both stones are annihilated. If the weights are not equal, the heavier stone's weight is reduced by the lighter stone's weight. The function should return the weight of the last remaining stone, or 0 if no stones are left. The input list `stones` will have a length between 1 and 30, and each weight will be a positive integer between 1 and 1000.
"""

import heapq

def lastStoneWeight(stones):
    stones = [-x for x in stones]
    heapq.heapify(stones)
    
    while len(stones) > 1:
        y = -heapq.heappop(stones)
        x = -heapq.heappop(stones)
        if y != x:
            heapq.heappush(stones, -abs(y-x))

    return -stones[0] if stones else 0