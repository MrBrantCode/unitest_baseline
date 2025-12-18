"""
QUESTION:
Write a function `sort_tasks(tasks)` that takes an array of dictionaries, each representing a task with keys "priority", "name", and "id", and returns the sorted array based on the following conditions: tasks with priority 1 come first, tasks with priority 10 come last, tasks with priority 2-9 are sorted by "name" and then "id", and tasks with the same priority and name are sorted by "id".
"""

def sort_tasks(tasks):
    priority_1 = [task for task in tasks if task["priority"] == 1]
    priority_2_9 = [task for task in tasks if 2 <= task["priority"] <= 9]
    priority_10 = [task for task in tasks if task["priority"] == 10]
    
    priority_2_9.sort(key=lambda x: (x["name"], x["id"]))
    
    return priority_1 + priority_2_9 + priority_10