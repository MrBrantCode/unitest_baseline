"""
QUESTION:
Implement a recursive function `print_keys_reverse` that takes a dictionary as input and prints its keys in reverse alphabetical order, but only for keys with values greater than 1. The function should not use any built-in sorting or filtering functions.
"""

def print_keys_reverse(dictionary):
    keys = list(dictionary.keys())
    n = len(keys)
    if n == 0:
        return
    max_key = keys[0]
    for key in keys:
        if key > max_key:
            max_key = key
    if dictionary[max_key] > 1:
        print(max_key)
    del dictionary[max_key]
    print_keys_reverse(dictionary)