"""
QUESTION:
Write a function called `tuple_to_dict` that converts a given tuple into a dictionary, where each key-value pair consists of adjacent elements from the tuple. If the tuple has an odd length, ignore the last element. If the tuple contains duplicate keys, append the values to the existing key in the form of a list.
"""

def tuple_to_dict(tup):
    # defining empty dictionary
    d = {}

    # Ignore last element if tuple has odd length
    if len(tup)%2 != 0:
        tup = tup[:-1]

    # iterating tuple
    for i in range(0, len(tup), 2):
        # checking if element exists as key or not
        if tup[i] in d:
            # if key exists, appending the value
            d[tup[i]].append(tup[i+1])
        else:
            d[tup[i]] = [tup[i+1]]

    # convert single-element lists to single values
    for key, value in d.items():
        if len(value) == 1:
            d[key] = value[0]

    return d