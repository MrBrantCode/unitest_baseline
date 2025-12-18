"""
QUESTION:
Create a function `inverse_dict` that takes a dictionary as input and returns its inverse. The original dictionary may contain duplicate values, so the inverse dictionary should store all the keys associated with a particular value in a list. The implementation should have a time complexity of O(n), where n is the number of key-value pairs in the original dictionary.
"""

def inverse_dict(dictionary):
    inverse = {}
    for key, value in dictionary.items():
        if value not in inverse:
            inverse[value] = [key]
        else:
            inverse[value].append(key)
    return inverse