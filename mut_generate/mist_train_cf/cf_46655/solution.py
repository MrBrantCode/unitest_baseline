"""
QUESTION:
Develop a function `flatten` that takes a nested list of arbitrary depth as input and returns a single linear list. The function should handle edge cases, such as empty lists. Additionally, create a function `add_structure` that takes the flattened list and the original nested list structure as input and returns the reconstituted original nested list. The original nested list structure should remain unchanged during the process.
"""

def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result += flatten(i)
        else:
            result.append(i)
    return result

def add_structure(source_lst, structure_lst):
    cloned_list = copy.deepcopy(structure_lst)
    iterator = iter(source_lst)
    def helper(current_lst):
        for i in range(len(current_lst)):
            if isinstance(current_lst[i], list):
                helper(current_lst[i])
            else:
                current_lst[i] = next(iterator)
    helper(cloned_list)
    return cloned_list