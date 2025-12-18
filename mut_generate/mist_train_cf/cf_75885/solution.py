"""
QUESTION:
Write a function `getSkyline` that takes a list of buildings as input, where each building is represented as a tuple of three integers `(L, R, H)` denoting the left coordinate, right coordinate, and height of the building, respectively. The function should return a list of points representing the skyline, where each point is a tuple `(x, h)` representing the x-coordinate and height of the point in the skyline. The function should implement a tie breaker logic to handle cases where two or more buildings have the same x-coordinate. The input list of buildings can be empty, and the output list of points should not include the initial point `(0, 0)`.
"""

import heapq

def getSkyline(buildings):
    events = [(L, -H, R) for L, R, H in buildings]
    events += [(R, 0, 0) for _, R, _ in buildings]
    
    events.sort()

    res = [(0, 0)]  
    live = [(0, float('inf'))]  
    for pos, negH, R in events:
        while live[0][1] <= pos:  
            heapq.heappop(live)
        if negH:  
            heapq.heappush(live, (negH, R))
        if res[-1][1] != -live[0][0]:  
            res += [(pos, -live[0][0])]
    return res[1:]  