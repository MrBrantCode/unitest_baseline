"""
QUESTION:
Create a function `get_unique_items` that takes a list of mixed data types as input and returns a list of items that appear only once. The input list can be of any size and may contain integers, floats, and strings. The function should handle these data types and return the correct output.
"""

def get_unique_items(lst):
    unique_items = []
    for item in lst:
        if lst.count(item) == 1:
            unique_items.append(item)
    return unique_items