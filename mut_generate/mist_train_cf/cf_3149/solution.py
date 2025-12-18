"""
QUESTION:
Write a function `string_indices(lst)` that takes a list of strings as input and returns a dictionary where each key is a string from the list and its corresponding value is a list of indices where the string occurs in the list. The function must maintain case sensitivity and have a time complexity of O(n), where n is the length of the input list.
"""

def string_indices(lst):
    indices_dict = {}
    for i, string in enumerate(lst):
        if string not in indices_dict:
            indices_dict[string] = [i]
        else:
            indices_dict[string].append(i)
    return indices_dict