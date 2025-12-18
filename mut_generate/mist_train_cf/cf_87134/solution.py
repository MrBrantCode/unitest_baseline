"""
QUESTION:
Create a function named `sort_tasks` that takes a list of tasks as input, where each task is a dictionary containing "priority", "name", and "id" keys. The function should sort the tasks based on the following conditions: 
- Tasks with a priority of 1 come first, 
- tasks with a priority of 10 come last, 
- tasks with a priority between 2 and 9 are sorted by "name" in ascending order, and 
- tasks with the same priority and name are sorted by "id" in ascending order. 

The function should return the sorted list of tasks.
"""

def sort_tasks(tasks):
    priority_1 = []
    priority_2_9 = []
    priority_10 = []
    
    for task in tasks:
        if task["priority"] == 1:
            priority_1.append(task)
        elif task["priority"] == 10:
            priority_10.append(task)
        else:
            priority_2_9.append(task)
    
    priority_2_9.sort(key=lambda x: (x["name"], x["id"]))
    
    return priority_1 + priority_2_9 + priority_10