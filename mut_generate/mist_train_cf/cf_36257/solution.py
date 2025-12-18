"""
QUESTION:
Write a function `highest_top_left` that takes a dictionary `json_obj` as input where each key is a string representing the name of a rectangle, and each value is a tuple representing the coordinates of the top-left corner of the rectangle in the form (x, y). The function should return the name of the rectangle with the highest y-coordinate for its top-left corner. If there are multiple rectangles with the same highest y-coordinate, return a list of their names in lexicographical order. The input dictionary can have between 1 and 10^5 key-value pairs, and the x and y coordinates can be any integers between -10^6 and 10^6.
"""

from typing import Union, List, Dict

def highest_top_left(json_obj: Dict[str, tuple]) -> Union[str, List[str]]:
    max_y = max(coord[1] for coord in json_obj.values())
    highest_rectangles = [name for name, coord in json_obj.items() if coord[1] == max_y]
    if len(highest_rectangles) == 1:
        return highest_rectangles[0]
    else:
        return sorted(highest_rectangles)