"""
QUESTION:
Write a function `convert_list_to_dictionary` that takes a list of items as input and returns a dictionary where each key is an item from the list and its corresponding value is the item's first occurrence position in the list. The dictionary should exclude duplicate items, and its items should be sorted in descending order based on their values. If two values are equal, the corresponding keys should be sorted alphabetically in ascending order.
"""

def convert_list_to_dictionary(lst):
    unique_items = []
    positions = {}
    
    # Iterate through the list and keep track of the first occurrence of each item and its position
    for i, item in enumerate(lst):
        if item not in unique_items:
            unique_items.append(item)
            positions[item] = i
    
    # Sort the dictionary in descending order based on the values. If two values are equal, sort them alphabetically in ascending order
    sorted_dict = dict(sorted(positions.items(), key=lambda x: (-x[1], x[0])))

    return sorted_dict