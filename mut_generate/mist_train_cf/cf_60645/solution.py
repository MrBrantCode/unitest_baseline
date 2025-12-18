"""
QUESTION:
Create a Python function `create_tuple` that generates a tuple with eight distinct values from a given list. If the list has fewer than eight distinct values, return `Not possible`. The function should account for the immutability of tuples in Python.
"""

def create_tuple(source_list):
    temp_set = set(source_list)
    if len(temp_set) < 8:
        return 'Not possible'
    temp_list = list(temp_set)
    result_tuple = ()
    for i in range(8):
        result_tuple += (temp_list.pop(),)
    return result_tuple