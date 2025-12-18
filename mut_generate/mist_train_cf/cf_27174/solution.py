"""
QUESTION:
Create a function `calculate_waterway_lengths(waterways)` that takes a list of waterway tuples, where each tuple contains the name of the waterway as a string and its length as an integer. The function should return a dictionary where the keys are the names of the waterways and the values are the total lengths of the waterways. If a waterway name appears more than once in the input list, the length in the output dictionary should be the sum of all occurrences of that waterway.
"""

def calculate_waterway_lengths(waterways):
    waterway_lengths = {}
    for name, length in waterways:
        if name in waterway_lengths:
            waterway_lengths[name] += length
        else:
            waterway_lengths[name] = length
    return waterway_lengths