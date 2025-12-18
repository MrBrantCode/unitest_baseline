"""
QUESTION:
Construct a Python function `embed_value` that takes in three parameters: `value`, `index_path`, and `nested_list`. The function should embed the `value` into the `nested_list` at the location specified by the `index_path`, which is a list of indices. The function should be able to handle recursively nested lists. The function can modify the original list.
"""

def embed_value(value, index_path, nested_list):
    current_index = index_path.pop(0)

    if len(index_path) == 0:
        nested_list[current_index] = value
    else:
        embed_value(value, index_path, nested_list[current_index])
    
    return nested_list