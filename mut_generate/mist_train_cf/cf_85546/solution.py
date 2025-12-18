"""
QUESTION:
Create a function called `flatten` that takes a nested list as input and returns a flat list without using built-in Python methods like `extend()` or `append()`. The function should handle non-list elements in the input by skipping them and printing an error message.
"""

def flatten(nested_list):
    flat_list = []
    for i in nested_list:
        if isinstance(i, list):
            flat_list += flatten(i)
        else:
            try:
                flat_list += [i]
            except TypeError:
                print(f'Element {i} is not list or list item!')
                continue
    return flat_list