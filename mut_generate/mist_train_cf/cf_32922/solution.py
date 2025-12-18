"""
QUESTION:
Write a function `count_input_output_types` that takes a tuple of TFLite model input and output types as input and returns a dictionary containing the count of each input and output type present in the tuple. The keys of the dictionary should be the input and output types, and the values should be the count of each type in the input tuple. The input tuple will only contain valid TFLite model input and output types.
"""

from collections import defaultdict

def count_input_output_types(types_tuple):
    type_count = defaultdict(int)
    for t in types_tuple:
        type_count[t] += 1
    return dict(type_count)