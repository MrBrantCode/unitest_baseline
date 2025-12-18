"""
QUESTION:
Given a list of projects with their respective profits and capitals, a maximum number of projects k that can be undertaken, and the initial capital W, write a function `findMaximizedCapital(k, W, Profits, Capital)` to maximize the total capital by selecting and completing up to k distinct projects. The function should return the maximized final capital.

Assume all numbers in the input are non-negative integers, the length of Profits array and Capital array will not exceed 50,000, and the solution fits in a 32-bit signed integer.
"""

import heapq

def findMaximizedCapital(k, W, Profits, Capital):
    projects = sorted(zip(Profits, Capital), key=lambda x: x[1])
    max_heap = []
    i = 0
    for _ in range(k):
        while i < len(projects) and projects[i][1] <= W:
            heapq.heappush(max_heap, -projects[i][0])
            i += 1
        if max_heap:
            W += -heapq.heappop(max_heap)
        else:
            break
    return W