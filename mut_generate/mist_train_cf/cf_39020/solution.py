"""
QUESTION:
Implement the `execute_tasks` function which takes in a list of tasks, each represented by a dictionary containing task information, and returns a list of task names in the order they were executed. 

Each task dictionary has the following keys: "name", "status", and "dependencies". The function should execute tasks based on the following rules:
- Tasks with no dependencies can be executed immediately.
- Tasks with dependencies can only be executed after all their dependencies have been completed.
- Tasks can only be executed if their status is "pending".

The function should not include any input validation or error handling beyond what is specified by the rules above.
"""

from typing import List, Dict, Union

def execute_tasks(tasks: List[Dict[str, Union[str, List[str]]]]) -> List[str]:
    task_map = {task["name"]: task for task in tasks}
    executed_tasks = []

    def execute_task(task_name):
        if task_name not in executed_tasks:
            task = task_map[task_name]
            for dependency in task["dependencies"]:
                execute_task(dependency)
            if task["status"] == "pending":
                executed_tasks.append(task_name)

    for task in tasks:
        execute_task(task["name"])

    return executed_tasks