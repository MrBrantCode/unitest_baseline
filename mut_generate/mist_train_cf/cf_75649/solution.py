"""
QUESTION:
Construct a function named `find_str` that takes two parameters: `info`, a list containing nested lists of varying lengths, and `y`, a string. The function should return a list of tuples representing the index positions of all instances of `y` within the overall `info` list. Each tuple should consist of two elements: row and index, signifying the location where `y` is found. The tuples should be arranged in ascending order based on the index positions within each nested list.
"""

def find_str(info, y):
    result = [(i, j) for i, sub_list in enumerate(info) for j, val in enumerate(sub_list) if val == y]
    return result