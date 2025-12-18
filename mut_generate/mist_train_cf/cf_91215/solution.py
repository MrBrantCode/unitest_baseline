"""
QUESTION:
Define a function `sort_key` that takes a dictionary as input, where the dictionary contains a "priority" key, and returns a value that can be used to sort a list of such dictionaries. The function should assign the lowest possible value to tasks with a priority of 1 and the highest possible value to tasks with a priority of 10, while maintaining the original priority order for all other tasks.
"""

def sort_key(task):
    priority = task["priority"]
    if priority == 1:
        return 0  
    elif priority == 10:
        return 11  
    else:
        return priority