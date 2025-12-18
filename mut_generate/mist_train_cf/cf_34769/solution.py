"""
QUESTION:
Write a function `calculate_completion_percentage(tasks: dict) -> float` that takes a dictionary `tasks` with task identifiers as keys and boolean values indicating task completion. The function should return the percentage of completed tasks as a float rounded to two decimal places. Assume the input dictionary contains at least one task.
"""

def calculate_completion_percentage(tasks: dict) -> float:
    completed_tasks = sum(1 for task_completed in tasks.values() if task_completed)
    total_tasks = len(tasks)
    completion_percentage = (completed_tasks / total_tasks) * 100
    return round(completion_percentage, 2)