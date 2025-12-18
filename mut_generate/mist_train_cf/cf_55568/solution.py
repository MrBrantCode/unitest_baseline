"""
QUESTION:
Create a Python function `find_str` that takes two arguments: a list of lists (`info`) and a string (`y`). The function should return a list of tuples representing the index positions where `y` is found within `info`. Each tuple should be in the format `(row, index)`, where `row` is the index of the sublist and `index` is the index of `y` within that sublist. If `y` appears multiple times within the same sublist, the corresponding tuples should be arranged in ascending order of their indices.
"""

def find_str(info, y):
    result = []
    for i, sub_list in enumerate(info):
        for j, item in enumerate(sub_list):
            if item == y:
                result.append((i, j))
    return result