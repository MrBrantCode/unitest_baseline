"""
QUESTION:
Implement the `choose_robots` function, which takes a boolean parameter `exclude_bimanual` and returns a list of robot configurations. The function should exclude bimanual robots from the selection if `exclude_bimanual` is True. Implement the `choose_task` function, which takes no parameters and returns a selected task. The functions should operate based on predefined lists of available robot configurations and tasks.
"""

def choose_robots(exclude_bimanual):
    available_robots = [
        {"name": "Single-arm A", "type": "single"},
        {"name": "Single-arm B", "type": "single"},
        {"name": "Bimanual-arm C", "type": "bimanual"},
        {"name": "Bimanual-arm D", "type": "bimanual"}
    ]

    if exclude_bimanual:
        available_robots = [robot for robot in available_robots if robot["type"] == "single"]

    return [robot["name"] for robot in available_robots]

def choose_task():
    available_tasks = ["Task 1", "Task 2", "Task 3", "Task 4"]
    selected_task = available_tasks[0]
    return selected_task