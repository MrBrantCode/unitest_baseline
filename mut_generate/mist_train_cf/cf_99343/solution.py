"""
QUESTION:
Write a function `sort_objects` that sorts a list of objects by color (red, green, blue) and then by size (small to large). Each object is a dictionary with 'name', 'color', 'size', and 'rgb' keys. The function should return a sorted list of objects and include the RGB values of each color in the output.
"""

def sort_objects(objects):
    color_order = {"red": 0, "green": 1, "blue": 2}
    return sorted(objects, key=lambda x: (color_order[x["color"]], x["size"]))