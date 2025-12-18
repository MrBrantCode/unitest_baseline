"""
QUESTION:
Create a function called `sort_objects` that sorts a list of objects by color (in the order of red, green, blue) and then by size (from smallest to largest). Each object is a dictionary containing the keys 'name', 'color', 'size', and 'rgb'. The function should return a table-formatted string containing the sorted list of objects with columns for 'Name', 'Color', 'Size', and 'RGB'.
"""

def sort_objects(objects):
    """
    Sorts a list of objects by color (in the order of red, green, blue) and then by size (from smallest to largest).
    
    Args:
        objects (list): A list of dictionaries containing the keys 'name', 'color', 'size', and 'rgb'.
    
    Returns:
        str: A table-formatted string containing the sorted list of objects with columns for 'Name', 'Color', 'Size', and 'RGB'.
    """
    # Define the color order
    color_order = {"red": 0, "green": 1, "blue": 2}
    
    # Sort the objects by color and then by size
    sorted_objects = sorted(objects, key=lambda x: (color_order[x["color"]], x["size"]))
    
    # Create the table header
    table = "{:<10} {:<10} {:<10} {}\n".format("Name", "Color", "Size", "RGB")
    
    # Add each object to the table
    for obj in sorted_objects:
        table += "{:<10} {:<10} {:<10} {}\n".format(obj["name"], obj["color"], obj["size"], obj["rgb"])
    
    return table