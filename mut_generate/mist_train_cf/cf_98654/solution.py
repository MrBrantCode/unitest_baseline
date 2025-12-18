"""
QUESTION:
Create a function called `sort_objects` that takes a list of objects as input, where each object has a "name", "color", "size", and "rgb" key. The function should sort the objects first by "color" (in the order of "red", "green", "blue") and then by "size" in ascending order. The function should return the sorted list of objects.
"""

def sort_objects(objects):
    """
    Sorts a list of objects by color and then by size.

    Args:
        objects (list): A list of objects with "name", "color", "size", and "rgb" keys.

    Returns:
        list: The sorted list of objects.
    """
    color_order = {"red": 0, "green": 1, "blue": 2}
    return sorted(objects, key=lambda x: (color_order[x["color"]], x["size"]))