"""
QUESTION:
Convert a list of integers to a dictionary with unique keys and their squares as values. 

Write a function `convert_list_to_dict` that takes a list of integers as input and returns a dictionary. The dictionary should have unique integers from the list as keys and their squares as values. The function should be efficient enough to handle large input lists.
"""

def convert_list_to_dict(lst):
    result_dict = {}
    unique_set = set(lst)
    for item in unique_set:
        result_dict[item] = item ** 2
    return result_dict