"""
QUESTION:
Write a function `get_oldest_parent` that selects the name, age, and address of the person with the most children from a database of persons and their children, returning only the person with the highest count of children. The person must have at least one child.
"""

def get_oldest_parent(persons, children):
    """
    Selects the name, age, and address of the person with the most children.

    Args:
    persons (dict): A dictionary of persons where each key is a person's ID and each value is another dictionary containing the person's name, age, and address.
    children (dict): A dictionary where the keys are parent IDs and the values are lists of child IDs.

    Returns:
    dict: A dictionary containing the name, age, and address of the person with the most children.
    """

    # Initialize a variable to store the parent with the most children
    oldest_parent = None
    max_children = 0

    # Iterate over each parent and their children
    for parent_id, child_ids in children.items():
        # Get the parent's information
        parent_info = persons.get(parent_id)

        # If the parent exists and has more children than the current oldest parent, update the oldest parent
        if parent_info and len(child_ids) > max_children:
            max_children = len(child_ids)
            oldest_parent = parent_info

    # Return the oldest parent
    return oldest_parent