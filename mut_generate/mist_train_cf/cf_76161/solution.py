"""
QUESTION:
Write a function `advanced_monotonic` that checks if the elements in a given list rise or fall monotonically. The function should take three parameters: `l` (the input list), `strict` (a boolean indicating whether the sequence should be strictly increasing or decreasing), and `ignore_non_numerical` (a boolean indicating whether to ignore non-numerical elements). 

The function should return `True` if the list is monotonic and `False` otherwise. If `strict` is `True`, the sequence should be strictly increasing or decreasing, meaning that neighboring elements must differ. If `ignore_non_numerical` is `True`, non-numerical elements should be skipped; otherwise, they should cause the function to return `False`. A non-numerical element is any element that is not an integer, a floating-point number, or a string that can be converted to a number.
"""

def advanced_monotonic(l: list, strict: bool = False, ignore_non_numerical: bool = False):
    valid_list = []

    for element in l:
        if type(element) in (int, float) or (isinstance(element, str) and element.replace('.', '', 1).replace('-', '', 1).isdigit()):
            valid_list.append(float(element))
        elif not ignore_non_numerical:
            return False

    if valid_list:
        if strict:  
            return all(valid_list[i] < valid_list[i + 1] for i in range(len(valid_list)-1)) or \
                all(valid_list[i] > valid_list[i + 1] for i in range(len(valid_list) - 1))
        else:  
            return all(valid_list[i] <= valid_list[i + 1] for i in range(len(valid_list) - 1)) or \
                all(valid_list[i] >= valid_list[i + 1] for i in range(len(valid_list) - 1))
    return False