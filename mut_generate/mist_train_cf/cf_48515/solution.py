"""
QUESTION:
Write a function `find_nearest(nums, target, k)` that takes a list of integers `nums`, a target value `target`, and an integer `k` as input. The function should return the `k` nearest integers in `nums` to `target`. If there are multiple closest values, follow the priority rule: same side (smaller or larger), opposite side (smaller, larger), and in case of two equally eligible values from the same side, choose the smaller one. Return the result in ascending order. If `k` is larger than the length of `nums`, return all values in `nums` in ascending order.
"""

import heapq

def find_nearest(nums, target, k):
    queue = []
    for num in nums:
        diff = abs(num - target)
        direction = 0 if num < target else 1
        heapq.heappush(queue, (diff, direction, num))
    return sorted([heapq.heappop(queue)[2] for _ in range(min(k, len(queue)))])

# Optimized version with O(n log k) complexity
def find_nearest_optimized(nums, target, k):
    queue = []
    for num in nums:
        diff = abs(num - target)
        direction = 0 if num < target else 1
        heapq.heappush(queue, (-diff, -direction, num))
        if len(queue) > k: heapq.heappop(queue)
    return sorted([heapq.heappop(queue)[2] for _ in range(len(queue))])