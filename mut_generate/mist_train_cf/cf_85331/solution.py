"""
QUESTION:
Given a list of project complexities, the number of days, and a list of constraints for each day, find the minimum complexity of a project plan that can be completed within the given timeframe. The complexity of each day is determined by the maximum complexity of a project completed on that day. The constraints list signifies the maximum complexity of a project that can be finalized on each day. Return the minimum complexity of the project plan if possible, otherwise return -1.

The function `minProjectComplexity` takes in three parameters: `projectComplexity`, a list of integers representing the complexities of the projects; `d`, the number of days to complete the projects; and `constraints`, a list of integers representing the maximum complexity of a project that can be finalized on each day. The function returns an integer representing the minimum complexity of the project plan.

Constraints: 1 <= projectComplexity.length <= 300, 0 <= projectComplexity[i] <= 1000, 1 <= d <= 10, 1 <= constraints.length <= d, 0 <= constraints[i] <= 1000
"""

import heapq

def minProjectComplexity(projectComplexity, constraints, d):
    if len(projectComplexity) < d:
        return -1

    projectComplexity.sort(reverse=True)
    constraints.sort()

    projects = []

    for complexity in projectComplexity:
        heapq.heappush(projects, -complexity)
        if len(projects) > len(constraints):
            heapq.heappop(projects)

    while projects:
        if -projects[0] > constraints.pop():
            return -1
        else:
            heapq.heappop(projects)

    return -sum(projects)