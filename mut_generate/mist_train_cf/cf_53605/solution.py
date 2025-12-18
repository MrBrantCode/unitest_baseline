"""
QUESTION:
Find the index of a given element in a list of lists, returning both the index of the sublist and the index of the element within that sublist. The function should return (-1, -1) if the element is not found.

The function should be named `find_index` and take two parameters: `input_list` and `target`.
"""

def find_index(input_list, target):
    for i in range(len(input_list)):
        if target in input_list[i]: 
            return (i, input_list[i].index(target))
    return (-1, -1)