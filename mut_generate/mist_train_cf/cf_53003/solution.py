"""
QUESTION:
Design a function called `get_old_objects` that takes two inputs: a set of objects, each with a 'date' property, and a comparison date. The function should return a list of objects whose 'date' property is less than the comparison date.
"""

def get_old_objects(objects, comparison_date):
    """
    Returns a list of objects whose 'date' property is less than the comparison date.

    Args:
        objects (list): A list of objects, each with a 'date' property.
        comparison_date (date): The date against which the object's dates will be compared.

    Returns:
        list: A list of objects whose 'date' property is less than the comparison date.
    """
    old_objects = [obj for obj in objects if obj['date'] < comparison_date]
    return old_objects