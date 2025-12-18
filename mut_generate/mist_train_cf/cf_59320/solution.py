"""
QUESTION:
Implement a function `pop_nested(input_list)` that takes a list as input and returns the modified list with the last element removed, including nested lists. If the last nested list becomes empty after removing the element, remove that list as well.
"""

def pop_nested(input_list):
    # Base case: if the input list is empty.
    if len(input_list) == 0:
        return input_list

    last_item = input_list[-1]
    
    # If the last item is list, apply this function recursively.
    if isinstance(last_item, list):
        pop_nested(last_item)
        # If the last item becomes empty after popping, remove it.
        if len(last_item) == 0:
            input_list.pop()

    # If the last item is not list, simply pop it.
    else:
        input_list.pop()

    return input_list