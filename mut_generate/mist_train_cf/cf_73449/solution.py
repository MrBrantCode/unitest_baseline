"""
QUESTION:
Create a function `index_dict` that accepts two lists, `first_list` and `second_list`, and returns a dictionary. Each key in the dictionary should be a unique element from `second_list` that exists in `first_list`. The corresponding value for each key should be a tuple containing two lists: the first list contains the indices of all occurrences of the element in `first_list`, and the second list contains the indices of all occurrences of the element in `second_list`. If an element from `second_list` does not exist in `first_list`, it should still be included in the dictionary with an empty list as the first list in the tuple.
"""

def index_dict(first_list, second_list):
    dictionary = {}
    for i in set(second_list):
        first_indices = [index for index, value in enumerate(first_list) if value == i]
        second_indices = [index for index, value in enumerate(second_list) if value == i]
        dictionary[i] = (first_indices, second_indices)
    return dictionary