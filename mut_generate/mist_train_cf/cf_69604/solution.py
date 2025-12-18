"""
QUESTION:
Write a function `dictionary_to_lists(d)` that takes a dictionary `d` with integer keys and mixed values (integers, floats, strings) and returns two lists of tuples. The first list should contain all key-value pairs from the dictionary in the order (key, value). The second list should contain only key-value pairs where the value is a string.
"""

def dictionary_to_lists(d):
    # declare list to hold all tuples
    all_tuples = []
    # declare list to hold tuples with strings only
    string_tuples = []
    for key, value in d.items():
        pair = (key, value)
        all_tuples.append(pair)
        if type(value) == str:
            string_tuples.append(pair)
    return all_tuples, string_tuples