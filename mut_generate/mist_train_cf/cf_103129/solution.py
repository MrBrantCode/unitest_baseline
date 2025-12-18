"""
QUESTION:
Create a function named 'sort_people' to sort a dictionary of people by age in ascending order. The dictionary should have a minimum of 5 entries, each containing 'name' (string), 'age' (integer), and 'hometown' (string) as keys. The function should return the sorted dictionary.
"""

def sort_people(people):
    """
    Sorts a dictionary of people by age in ascending order.

    Args:
        people (dict): A dictionary containing information about people.
            Each entry should have 'name' (string), 'age' (integer), and 'hometown' (string) as keys.

    Returns:
        dict: The sorted dictionary of people by age in ascending order.
    """
    return dict(sorted(people.items(), key=lambda x: x[1]['age']))