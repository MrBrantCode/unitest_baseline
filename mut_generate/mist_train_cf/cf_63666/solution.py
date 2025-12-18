"""
QUESTION:
Write a function `find_element` that takes an array of integers as input, where the numbers 1 to 13 appear exactly twice and checks if the number 15 is present in the array. If 15 is present, return a tuple containing `True` and a list of indices where 15 is found. If 15 is not present, return a tuple containing `False`.
"""

def entance(array):
    index_list = []
    for i, val in enumerate(array):
        if val == 15:
            index_list.append(i)
    if index_list:
        return (True, index_list)
    else:
        return (False,)