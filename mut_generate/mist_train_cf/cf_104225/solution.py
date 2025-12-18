"""
QUESTION:
Create a function named `custom_sort` that sorts a list of dictionaries based on the following criteria: tasks with a priority of 1 come first, tasks with a priority of 10 come last, and tasks with a priority between 2 and 9 (inclusive) are sorted by name in ascending order. If two tasks have the same priority and name, the one with the lower "id" key comes first. The function should take a list of dictionaries as input where each dictionary contains "id", "name", and "priority" keys.
"""

def custom_sort(data):
    """
    Sorts a list of dictionaries based on the following criteria:
    - tasks with a priority of 1 come first
    - tasks with a priority of 10 come last
    - tasks with a priority between 2 and 9 (inclusive) are sorted by name in ascending order
    - if two tasks have the same priority and name, the one with the lower "id" key comes first

    Args:
        data (list): A list of dictionaries, each containing "id", "name", and "priority" keys.

    Returns:
        list: The sorted list of dictionaries.
    """

    return sorted(data, key=lambda x: (x["priority"], x["name"] if 1 < x["priority"] < 10 else '', x["id"]))