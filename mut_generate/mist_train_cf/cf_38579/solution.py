"""
QUESTION:
Implement a Python function `find_modes` that takes a list of integers as input and returns a list of tuples, where each tuple contains a mode value and its frequency. The function should return all mode values and their frequencies if there are multiple modes, and an empty list if there are no repeated values. The output list should be sorted in ascending order based on the mode values.
"""

def find_modes(data):
    mode_count = {}
    max_count = 0
    modes = []

    for value in data:
        if value in mode_count:
            mode_count[value] += 1
        else:
            mode_count[value] = 1

        if mode_count[value] > max_count:
            max_count = mode_count[value]

    for key, value in mode_count.items():
        if value == max_count:
            modes.append((key, value))

    return sorted(modes)