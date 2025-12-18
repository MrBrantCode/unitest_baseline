"""
QUESTION:
Write a function `remove_element(y, x)` that takes a list `y` and an element `x` as input, removes all occurrences of `x` from `y` while maintaining the original order of the remaining elements, and returns the new list. The function should have a time complexity of O(n), where n is the length of the list. If `x` is not present in `y`, the function should print an error message "Element {x} not found in the list." and return without modifying the list.
"""

def remove_element(y, x):
    if x not in y:
        print(f"Element {x} not found in the list.")
        return
    
    new_list = []
    for element in y:
        if element != x:
            new_list.append(element)
    
    return new_list