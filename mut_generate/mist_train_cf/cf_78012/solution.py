"""
QUESTION:
Implement the function `solve(n, m, category, beforeTasks)` that takes four parameters: `n`, the number of tasks; `m`, the number of categories; `category`, a list of length `n` where `category[i]` is the category of the `i`-th task, or `-1` if the task is not assigned to any category; and `beforeTasks`, a list of lists where `beforeTasks[i]` is a list of tasks that must precede the `i`-th task in the sorted list. 

The function should return a sorted list of tasks such that tasks belonging to the same category are adjacent in the sorted list, and tasks that must precede other tasks are ordered correctly. If no such ordering is possible, return an empty list.

Constraints: `1 <= m <= n <= 3 * 10^4`, `category.length == beforeTasks.length == n`, `-1 <= category[i] <= m - 1`, `0 <= beforeTasks[i].length <= n - 1`, `0 <= beforeTasks[i][j] <= n - 1`, `i != beforeTasks[i][j]`, and `beforeTasks[i]` does not contain duplicate elements.
"""

import collections
import heapq

def sortTasks(n, m, category, beforeTasks):
    NO_CATEGORY = m
    graph = collections.defaultdict(list)
    indegrees = collections.defaultdict(int)
    for task, beforeList in enumerate(beforeTasks):
        for before in beforeList:
            graph[before].append(task)
            indegrees[task] += 1
    pq = []
    for task in range(n):
        if indegrees[task] == 0:
            cat = category[task] if category[task] != -1 else NO_CATEGORY
            heapq.heappush(pq, (cat, task))
    
    res = []
    while pq:
        _, task = heapq.heappop(pq)
        res.append(task)
        for neig in graph[task]:
            indegrees[neig] -= 1
            if indegrees[neig] == 0:
                cat = category[neig] if category[neig] != -1 else NO_CATEGORY
                heapq.heappush(pq, (cat, neig))
    
    return res if len(res) == n else []