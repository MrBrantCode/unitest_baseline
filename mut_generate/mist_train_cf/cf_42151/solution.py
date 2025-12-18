"""
QUESTION:
Implement a function `parseColumnSizes` that takes a string representing a Bootstrap grid system class attribute and returns a list of tuples containing the screen size and the corresponding column size. 

The input class attribute is a string with classes separated by spaces, where each class is in the format "col-{screen-size}-{column-size}" or "col-{screen-size}-push-{push-size}". The screen size can be "xs", "sm", "md", or "lg", and the column size and push size are integers. 

The function should return a list of tuples, where each tuple contains the screen size and the corresponding column size or push size.
"""

from typing import List, Tuple

def parseColumnSizes(class_attribute: str) -> List[Tuple[str, int]]:
    column_sizes = []
    classes = class_attribute.split()
    for class_name in classes:
        if class_name.startswith('col-'):
            parts = class_name.split('-')
            screen_size = parts[1]
            if parts[2].isdigit():
                column_size = int(parts[2])
                column_sizes.append((screen_size, column_size))
            elif parts[2].startswith('push'):
                push_size = int(parts[3])
                column_sizes.append((f"{screen_size}-push", push_size))
    return column_sizes