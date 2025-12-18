"""
QUESTION:
Create a function called `sort_tasks` that sorts a list of tasks by their categories. Each task is represented as a dictionary with 'title', 'description', 'category', and 'due_date' keys. The function should return a dictionary where the keys are the categories and the values are lists of tasks belonging to each category.
"""

def sort_tasks(tasks):
    """
    Sorts a list of tasks by their categories.

    Args:
        tasks (list): A list of tasks. Each task is a dictionary with 'title', 'description', 'category', and 'due_date' keys.

    Returns:
        dict: A dictionary where the keys are the categories and the values are lists of tasks belonging to each category.
    """
    sorted_tasks = {}
    for task in tasks:
        category = task['category']
        if category not in sorted_tasks:
            sorted_tasks[category] = []
        sorted_tasks[category].append(task)
    return sorted_tasks