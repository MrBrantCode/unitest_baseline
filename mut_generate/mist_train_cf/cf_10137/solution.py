"""
QUESTION:
Write a function `sort_key` that takes a dictionary `task` as input and returns a sorting key value. The function should sort tasks by their "priority" key in ascending order, except for tasks with a priority of 1 which should be placed at the beginning of the list and tasks with a priority of 10 which should be placed at the end of the list.
"""

def sort_key(task):
    priority = task["priority"]
    if priority == 1:
        return 0  # Tasks with priority 1 should come first
    elif priority == 10:
        return 11  # Tasks with priority 10 should come last
    else:
        return priority