"""
QUESTION:
Write a function `calculate_online_time(actions: List[str]) -> Dict[str, int]` that takes in a list of strings `actions` representing the actions of each employee. The list contains strings "online", "offline", and "leave", indicating when an employee comes online, goes offline, or takes a break. The function should return a dictionary where the keys are the names of the employees (in this case, "employee1", "employee2", etc.) and the values are the total time each employee has spent online, considering the time between their first online action and their last offline action, excluding any time spent on breaks. Assume the input list `actions` will always contain an even number of elements and each employee's actions will be grouped together.
"""

from typing import List, Dict

def calculate_online_time(actions: List[str]) -> Dict[str, int]:
    online_time = {}
    current_employee = ""
    online_start = 0
    total_online_time = 0
    leave_count = 0
    for i, action in enumerate(actions):
        if action.startswith("employee"):
            if current_employee:
                online_time[current_employee] = total_online_time
            current_employee = action
            online_start = i
            total_online_time = 0
            leave_count = 0
        elif action == "online":
            online_start = i
        elif action == "offline":
            total_online_time += i - online_start - leave_count
        elif action == "leave":
            leave_count += 1
    if current_employee:
        online_time[current_employee] = total_online_time
    return online_time