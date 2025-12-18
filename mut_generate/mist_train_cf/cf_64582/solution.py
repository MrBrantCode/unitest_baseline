"""
QUESTION:
Write a function `invert_dict` that takes a dictionary as an input and returns a new dictionary with the keys and values inverted. If the input dictionary has non-unique values, the corresponding value in the new dictionary should be a list of keys from the original dictionary.
"""

def invert_dict(my_dict):
    inverted_dict = {}
    for key, value in my_dict.items():
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        else:
            inverted_dict[value].append(key)
    return inverted_dict