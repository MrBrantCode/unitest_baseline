"""
QUESTION:
Implement a function `minimum_completion_time(num_tasks, edges, build_time)` that calculates the minimum time required to complete all tasks in a project represented by a directed acyclic graph. The function should take three inputs: `num_tasks`, the number of tasks; `edges`, a list of tuples representing task dependencies; and `build_time`, a list of integers representing task completion times. The function should return the minimum time required to complete all tasks, considering that each task can only be started once all its prerequisites have been completed.
"""

from collections import defaultdict, deque

def min_completion_time(num_tasks, edges, build_time):
    orders = defaultdict(list)
    indegree = [0] * num_tasks
    rt = [0] * num_tasks

    for a, b in edges:
        orders[a].append(b)
        indegree[b] += 1

    q = deque()
    for i in range(num_tasks):
        if indegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        for next_task in orders[cur]:
            rt[next_task] = max(rt[next_task], rt[cur] + build_time[cur])
            indegree[next_task] -= 1
            if indegree[next_task] == 0:
                q.append(next_task)

    return max(rt)