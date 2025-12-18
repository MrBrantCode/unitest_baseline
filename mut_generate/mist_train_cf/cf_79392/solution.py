"""
QUESTION:
Create a function `getValue` that accepts a dictionary `dict_` and a key `key_` as inputs. The function should return the value corresponding to the input key if it exists in the dictionary. If the key does not exist, the function should return an error message. The input dictionary will contain string keys and integer values.
"""

def getValue(dict_, key_):
    try:
        return dict_[key_]
    except KeyError:
        return "Key not found in the dictionary"