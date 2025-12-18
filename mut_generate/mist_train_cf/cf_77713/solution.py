"""
QUESTION:
Write a function `find_positions` that takes two lists `first_list` and `second_list` as input, and returns a list of positions where elements from `second_list` are found in `first_list`. The positions should be 0-indexed, meaning the first element in `first_list` is at position 0. The function should return all positions where elements from `second_list` appear in `first_list`, even if the elements appear multiple times in `first_list`.
"""

def find_positions(first_list, second_list):
    positions = []
    for item in second_list:
        if item in first_list:
            positions.append(first_list.index(item))
    return positions