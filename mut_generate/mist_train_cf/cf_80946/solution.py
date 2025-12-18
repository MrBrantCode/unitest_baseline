"""
QUESTION:
Implement a function named `has_deadlock` that determines whether a system of processes and resources is in a deadlock state. The system is represented as a list of processes, where each process is a dictionary containing the resources it holds and the resources it is waiting for. The function should return True if the system is in a deadlock state and False otherwise. The function should not modify the input system.
"""

from collections import defaultdict, deque

def has_deadlock(processes):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for i, process in enumerate(processes):
        for resource in process['waiting']:
            graph[resource].append(i)
            in_degree[i] += 1

    queue = deque([i for i in range(len(processes)) if in_degree[i] == 0])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return any(in_degree.values())