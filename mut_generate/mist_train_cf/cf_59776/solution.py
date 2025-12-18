"""
QUESTION:
Given a characters array tasks and a non-negative integer n, return the least number of units of times that the CPU will take to finish all the given tasks, where there must be at least n units of time between any two same tasks. If it is not possible to schedule all tasks, return -1.

The tasks array consists of upper-case English letters and may contain more instances of a certain task than can be scheduled considering the cooldown period n. The constraints are 1 <= task.length <= 10^4 and 0 <= n <= 100.

Write a function leastInterval(tasks, n) that takes tasks and n as input and returns the least number of units of times required.
"""

import collections
import heapq

def leastInterval(tasks, n):
    curr_time, h = 0, []
    for k,v in collections.Counter(tasks).items():
        heapq.heappush(h, (-1*v, k))
    while h:
        i, temp = 0, []
        while i <= n:
            curr_time += 1
            if h:
                x,y = heapq.heappop(h)
                if x != -1:
                    temp.append((x+1,y))
            if not h and not temp:
                break
            else:
                i += 1
        for item in temp:
            heapq.heappush(h, item)
    return curr_time