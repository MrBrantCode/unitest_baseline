"""
QUESTION:
Create a function `remove_items_at_positions` that takes a list and a set of positions as input, and returns a new list containing the elements from the original list at positions not in the set. The function should not modify the original list.
"""

def remove_items_at_positions(original_list, positions_to_remove):
    return [elem for i, elem in enumerate(original_list) if i not in positions_to_remove]