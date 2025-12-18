"""
QUESTION:
Create a function named `create_dictionary` that takes two lists, `keys` and `values`, as input and returns a dictionary where the elements of `keys` are the keys and the elements of `values` are the corresponding values. The function should ignore any key that is an empty string or has a length greater than 10 characters. If there are duplicate keys, the last occurrence of the key will override the previous ones. The function should handle values of different data types.
"""

def create_dictionary(keys, values):
    dictionary = {}
    for i in range(len(keys)):
        key = keys[i]
        value = values[i]
        if key != "" and len(key) <= 10:
            dictionary[key] = value
    return dictionary