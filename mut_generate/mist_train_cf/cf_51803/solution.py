"""
QUESTION:
Given a 2D integer array `classes` where `classes[i] = [passi, totali]` and an integer `extraStudents`, allocate `extraStudents` to classes to maximize the average pass ratio. The pass ratio of a class is `passi / totali`. The average pass ratio is the sum of the pass ratios of all classes divided by the number of classes. Return the highest possible average pass ratio after assigning `extraStudents`. The constraints are `1 <= classes.length <= 105`, `classes[i].length == 2`, `1 <= passi < totali <= 105`, and `1 <= extraStudents <= 105`.
"""

import heapq

def maxAverageRatio(classes, extraStudents):
    maxheap = []
    
    for a, b in classes:
        diff = -a/b + (a+1) / (b+1)
        heapq.heappush(maxheap, (-diff, a, b))
    
    while extraStudents:
        diff, a, b = heapq.heappop(maxheap)
        diff = -a/b + (a+1) / (b+1)
        heapq.heappush(maxheap, (-diff, a+1, b+1))
        extraStudents -= 1

    total_ratio = sum(a/b for _, a, b in maxheap)
    
    return total_ratio / len(classes)