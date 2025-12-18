"""
QUESTION:
Create a function named `find_match` that takes two arguments: a numerical parameter `num` and a list of numerical parameters `num_list`. The function should return the index (or indices) of `num` in `num_list` if a match is found, with indexing starting from 0. If multiple matches are found, return all indices. If no match is found, return "No match found".
"""

def find_match(num, num_list):
    indices = [i for i, x in enumerate(num_list) if x == num]
    if indices:
        return indices
    else:
        return "No match found"