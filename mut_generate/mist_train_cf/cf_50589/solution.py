"""
QUESTION:
Combine the elements of multiple dictionaries into a single dictionary. If there are duplicate keys, increment the value by the sum of the values from the individual dictionaries. The function should take a list of dictionaries as input and return a single dictionary.
"""

def combine_dicts(dicts):
    combined_dict = {}
    for d in dicts:
        for k in d.keys():
            if k in combined_dict:
                combined_dict[k] += d[k]
            else:
                combined_dict[k] = d[k]
    return combined_dict