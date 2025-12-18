"""
QUESTION:
Write a function `inverse_dictionary(dictionary)` that takes a dictionary as input and returns a new dictionary where the keys and values are swapped. If there are duplicate values in the original dictionary, the corresponding keys should be stored in a list as the value in the new dictionary.
"""

def inverse_dictionary(dictionary):
    inversed_dictionary = {}
    for key, value in dictionary.items():
        if value in inversed_dictionary:
            inversed_dictionary[value].append(key)
        else:
            inversed_dictionary[value] = [key]
    return inversed_dictionary