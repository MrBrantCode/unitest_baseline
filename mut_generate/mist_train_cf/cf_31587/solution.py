"""
QUESTION:
Write a function named `min_completion_time` that takes two parameters: a list of unique task identifiers and a list of tuples representing the dependencies between tasks, where each tuple contains the identifier of the task on which the dependency depends, the identifier of the dependent task, and the time it takes to complete the dependency. The function should return the minimum time required to complete all the tasks, considering the dependencies and their associated weights.

The input parameters are:
- `tasks`: A list of unique task identifiers, where 2 <= len(tasks) <= 100.
- `dependencies`: A list of tuples representing the dependencies between tasks, where each tuple contains three elements:
  - The identifier of the task on which the dependency depends.
  - The identifier of the dependent task.
  - The time it takes to complete the dependency, where 0 <= time <= 100.

The function should return an integer representing the minimum time required to complete all the tasks.
"""

from typing import List, Tuple
from collections import defaultdict

def min_completion_time(tasks: List[str], dependencies: List[Tuple[str, str, int]]) -> int:
    graph = defaultdict(list)
    in_degree = {task: 0 for task in tasks}
    time_taken = {task: 0 for task in tasks}

    for dependency in dependencies:
        parent, child, time = dependency
        graph[parent].append((child, time))
        in_degree[child] += 1

    queue = [task for task in tasks if in_degree[task] == 0]

    while queue:
        current_task = queue.pop(0)
        for child, time in graph[current_task]:
            in_degree[child] -= 1
            time_taken[child] = max(time_taken[child], time_taken[current_task] + time)
            if in_degree[child] == 0:
                queue.append(child)

    return max(time_taken.values())