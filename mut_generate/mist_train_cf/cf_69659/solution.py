"""
QUESTION:
Write a Python function named `is_feasible` that implements a greedy algorithm to determine whether a given list of tasks can be completed within a specified time limit. The function takes two parameters: `tasks` (a list of tasks, where each task is a dictionary containing a 'name' and a 'duration' key) and `time_limit` (the maximum allowed time to complete all tasks). The function should return `True` if all tasks can be completed within the time limit and `False` otherwise.
"""

def is_feasible(tasks, time_limit):
    """
    This function determines whether a given list of tasks can be completed within a specified time limit.
    
    Parameters:
    tasks (list): A list of tasks, where each task is a dictionary containing a 'name' and a 'duration' key.
    time_limit (int): The maximum allowed time to complete all tasks.
    
    Returns:
    bool: True if all tasks can be completed within the time limit, False otherwise.
    """
    total_time = sum(task['duration'] for task in tasks)
    return total_time <= time_limit