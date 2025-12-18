"""
QUESTION:
Write a function called `inverse_dictionary` that takes a dictionary as input and returns a new dictionary where the keys and values are swapped. If there are duplicate values in the original dictionary, the corresponding keys should be stored in a list as the value in the new dictionary. The function should also remove any keys from the new dictionary that have a list with more than one value.
"""

def inverse_dictionary(dictionary):
    inversed_dictionary = {}
    for key, value in dictionary.items():
        if value not in inversed_dictionary:
            inversed_dictionary[value] = [key]
        else:
            inversed_dictionary[value].append(key)
    # Remove duplicate values
    inversed_dictionary = {key: value[0] for key, value in inversed_dictionary.items() if len(value) == 1}
    return inversed_dictionary