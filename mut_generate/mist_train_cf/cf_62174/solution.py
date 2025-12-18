"""
QUESTION:
Create a function named `replace_element` that takes a list (`initial_list`), an index, and a new element (`new_elem`) as arguments. The function should replace the element at the specified index in the list with the new element. If the index is out of range, the function should print an error message that includes the valid range of indices for the list. The function should return the modified list.
"""

def replace_element(initial_list, index, new_elem):
    try:
        initial_list[index] = new_elem
        print(f"Element at index {index} has been replaced with {new_elem}.")
    except IndexError:
        print(f"Index out of range. Please provide an index between 0 and {len(initial_list) - 1}.")
    return initial_list