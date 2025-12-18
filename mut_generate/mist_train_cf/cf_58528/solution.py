"""
QUESTION:
You are given an array of integers `projectComplexity`, an integer `d`, and an array of integers `constraints`. The task is to plan a series of projects in `d` days, where the complexity of the `i-th` project is `projectComplexity[i]` and the `i-th` constraint in `constraints` array represents the maximum complexity of a project that can be completed on the `i-th` day.

The goal is to find the minimum complexity of a project plan, where the complexity of a day is the maximum complexity of a project completed in that day, and at least one project must be completed every day. If no plan can be found, return -1.

The function should be named `minProjectComplexity` and should take three parameters: `projectComplexity`, `d`, and `constraints`. The function should return the minimum complexity of a project plan.

Restrictions:
- `1 <= projectComplexity.length <= 300`
- `0 <= projectComplexity[i] <= 1000`
- `1 <= d <= 10`
- `1 <= constraints.length <= d`
- `0 <= constraints[i] <= 1000`
"""

import heapq

def minProjectComplexity(projectComplexity, d, constraints):
    projectComplexity.sort(reverse=True)
    constraints.sort(reverse=True)
    queue = []
    total_complexity = 0
    j = 0
    for i in range(d):
        while j < len(projectComplexity) and projectComplexity[j] <= constraints[i]:
            heapq.heappush(queue, -projectComplexity[j])
            j += 1
        if queue:
            total_complexity += -heapq.heappop(queue)
        elif j < len(projectComplexity):
            return -1
    return total_complexity if j == len(projectComplexity) else -1