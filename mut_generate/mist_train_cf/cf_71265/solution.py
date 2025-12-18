"""
QUESTION:
Create a function called `replace_item` that takes three parameters: `original_list`, `old_item`, and `new_item`. The function should return a new list where all occurrences of `old_item` in `original_list` are replaced with `new_item`, without modifying the original list.
"""

def replace_item(original_list, old_item, new_item):
    return [new_item if item == old_item else item for item in original_list]