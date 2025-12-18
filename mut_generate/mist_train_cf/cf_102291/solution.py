"""
QUESTION:
Create a function `filter_by_state` that takes a list of dictionaries representing people and a state as input. Each dictionary contains keys "name", "age", and "address", where "address" is a nested dictionary with keys "street", "city", and "state". The function should return a new list of dictionaries containing only the people who live in the specified state, sorted by age in descending order and then by name in alphabetical order.
"""

def filter_by_state(data, state):
    """
    Filters a list of people by state and returns a new list sorted by age in descending order and then by name in alphabetical order.

    Args:
        data (list): A list of dictionaries representing people.
        state (str): The state to filter by.

    Returns:
        list: A new list of dictionaries containing only the people who live in the specified state, sorted by age and name.
    """
    return sorted([person for person in data if person["address"]["state"] == state], key=lambda x: (-x["age"], x["name"]))