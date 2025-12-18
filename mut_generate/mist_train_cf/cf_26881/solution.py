"""
QUESTION:
Create a function `execute_tasks` that takes in a list of tasks with their dependencies and the number of threads available for concurrent execution, and returns a list of task names in the order they were completed. Each task is represented as a tuple containing the task name and a list of its dependencies. The function should ensure that all dependencies for a task are completed before executing that task, and all tasks are independent and can be executed concurrently if their dependencies are met.
"""

from typing import List, Tuple
from concurrent.futures import ThreadPoolExecutor

def execute_tasks(tasks: List[Tuple[str, List[str]]], num_threads: int) -> List[str]:
    task_dependencies = {task[0]: task[1] for task in tasks}
    completed_tasks = set()
    execution_order = []

    def execute_task(task_name):
        if task_name not in completed_tasks:
            dependencies = task_dependencies[task_name]
            for dependency in dependencies:
                execute_task(dependency)
            completed_tasks.add(task_name)
            execution_order.append(task_name)

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for task_name in task_dependencies.keys():
            executor.submit(execute_task, task_name)

    return execution_order