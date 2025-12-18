"""
QUESTION:
Write a function `can_finish_project` that determines whether a project can be completed by a given deadline. The function takes in three parameters: `project_tasks`, a list of tasks where each task is an object with `time_needed` and `resources_needed` properties; `available_resources`, the total amount of resources available for the project; and `deadline`, the time by which the project must be completed. The function should return 'yes' if the project can be completed by the deadline and 'no' otherwise. The tasks should be prioritized based on their `time_needed` property, with tasks that require less time being completed first.
"""

import heapq

class Task:
    def __init__(self, time_needed, resources_needed):
        self.time_needed = time_needed
        self.resources_needed = resources_needed

    def __lt__(self, other):
        return self.time_needed < other.time_needed


def can_finish_project(project_tasks, available_resources, deadline):
    current_time = 0  
    task_heap = []

    for task in project_tasks:
        heapq.heappush(task_heap, task)

    while task_heap:
        current_task = heapq.heappop(task_heap)
        if current_time + current_task.time_needed > deadline:
            return "no"
        if current_task.resources_needed > available_resources:
            return "no"
        current_time += current_task.time_needed
        available_resources -= current_task.resources_needed

    return "yes"