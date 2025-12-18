"""
QUESTION:
Implement a function `task_execution_order(tasks, dependencies)` that takes in a list of task IDs (`tasks`) and a list of dependencies (`dependencies`) and returns a list of task IDs in a valid order for execution. Each dependency is a tuple (`task_id`, `dependent_task_id`), indicating that `dependent_task_id` depends on the completion of `task_id`. If there are multiple valid orders, return any valid order. If a cycle is detected in the dependencies, return an empty list.
"""

def task_execution_order(tasks, dependencies):
    graph = {task: [] for task in tasks}
    in_degree = {task: 0 for task in tasks}

    for dependency in dependencies:
        task, dependent_task = dependency
        graph[task].append(dependent_task)
        in_degree[dependent_task] += 1

    queue = [task for task in tasks if in_degree[task] == 0]
    execution_order = []

    while queue:
        current_task = queue.pop(0)
        execution_order.append(current_task)

        for dependent_task in graph[current_task]:
            in_degree[dependent_task] -= 1
            if in_degree[dependent_task] == 0:
                queue.append(dependent_task)

    if len(execution_order) != len(tasks):
        return []  # Cycle detected

    return execution_order