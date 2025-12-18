"""
QUESTION:
Create a function named `find_index` that takes two parameters: `target` and `array`. The function should return a list of all indices where the `target` element is found in the `array`. If the `target` is not found in the `array`, the function should return "Element not found." The function should be optimized for time complexity, avoiding duplicate traversals and unnecessary checking.
"""

def find_index(target, array):
    indices = [i for i, x in enumerate(array) if x == target]
    if indices:
        return indices
    else:
        return "Element not found."