"""
QUESTION:
Given an integer array `heights` representing the heights of buildings, an integer `bricks`, an integer `ladders`, and an integer `k`, return the furthest building index you can reach if you use the given ladders and bricks optimally. You can move to the next building by using bricks or ladders, and the rules for using bricks or ladders are as follows: 
- If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
- If the current building's height is less than the next building's height, you can either use one ladder or `(h[i+k] - h[i])` bricks.

Constraints: 
- `1 <= heights.length <= 10^5`
- `1 <= heights[i] <= 10^6`
- `0 <= bricks <= 10^9`
- `0 <= ladders <= heights.length`
- `1 <= k <= heights.length`
"""

import heapq

def furthestBuilding(heights, bricks, ladders, k):
    heap = []
    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        if diff > 0:
            heapq.heappush(heap, diff)
        if len(heap) > ladders:
            bricks -= heapq.heappop(heap)
        if bricks < 0:
            return i
    return len(heights) - 1