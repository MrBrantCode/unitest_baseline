"""
QUESTION:
Implement the function `count_interaction_modes(interaction_modes)` that takes a list of interaction modes as strings and returns a dictionary where the keys are unique interaction modes and the values are their respective counts.
"""

def count_interaction_modes(interaction_modes):
    mode_count = {}
    for mode in interaction_modes:
        if mode in mode_count:
            mode_count[mode] += 1
        else:
            mode_count[mode] = 1
    return mode_count